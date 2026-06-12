#!/usr/bin/env python3
"""
fix_gitbook_windows_paths.py
----------------------------
Documents and repeats the cleanup logic applied to this repository to fix
Windows-incompatible file/folder names produced by GitBook Korean exports.

Problem
~~~~~~~
GitBook exports for the Korean locale of smartbooks-erp-system created
directories whose names end with a period (e.g. "3.", "4.", "5.", "6.", "7.")
and files whose basenames end with a period before the extension
(e.g. "1..md", "3.4..md", "4.5..md", "5.4..md").
Windows forbids trailing dots in file/directory names; Git on Windows therefore
refuses to check out these paths with "error: invalid path".

Solution
~~~~~~~~
All Korean paths are renamed to match the English sibling slugs where a
one-to-one correspondence exists.  Korean display titles in SUMMARY.md are
kept unchanged.

This script:
  1. Checks the repository for any remaining Windows-invalid paths.
  2. Prints a summary of the renames that were performed.
  3. Verifies every local link in SUMMARY.md points to an existing file.

Run from the repository root:
    python scripts/fix_gitbook_windows_paths.py

The renames documented below were applied once via git mv and are therefore
already reflected in the working tree when you clone this repository.
"""

from __future__ import annotations

import os
import re
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

REPO_ROOT = Path(__file__).resolve().parent.parent

# Projects that have Korean sub-trees that were affected
PROJECTS = [
    "smartbooks-erp-system",
    "smartbooks-web-guideline",
    "smartbooks-windows-guideline",
    "smartbooks-hrm-guideline",
]

# Windows reserved names (case-insensitive)
RESERVED = {
    "CON", "PRN", "AUX", "NUL",
    *[f"COM{i}" for i in range(1, 10)],
    *[f"LPT{i}" for i in range(1, 10)],
}

# Windows-forbidden characters in path components
WIN_FORBIDDEN = re.compile(r'[<>:"/\\|?*]')

# ---------------------------------------------------------------------------
# Documented renames (old path → new path, relative to REPO_ROOT)
# ---------------------------------------------------------------------------
# These renames were applied once to fix the Windows-incompatible paths.
# The script reproduces this list for documentation / audit purposes.

RENAMES: list[tuple[str, str]] = [
    # ---- smartbooks-erp-system / korean ---------------------------------
    # Root file
    (
        "smartbooks-erp-system/korean/1..md",
        "smartbooks-erp-system/korean/1.-login.md",
    ),
    # 2. SETUP TOOLS directory
    (
        "smartbooks-erp-system/korean/2/2.1.md",
        "smartbooks-erp-system/korean/2.-setup-tools/2.1-change-password.md",
    ),
    (
        "smartbooks-erp-system/korean/2/2.2.md",
        "smartbooks-erp-system/korean/2.-setup-tools/2.2-company-information.md",
    ),
    # 3. SALE ORDER MODULE
    (
        "smartbooks-erp-system/korean/2/3./README.md",
        "smartbooks-erp-system/korean/2.-setup-tools/3-sale-order-module/README.md",
    ),
    (
        "smartbooks-erp-system/korean/2/3./3.1.md",
        "smartbooks-erp-system/korean/2.-setup-tools/3-sale-order-module/3.1-customer-list.md",
    ),
    (
        "smartbooks-erp-system/korean/2/3./3.2.md",
        "smartbooks-erp-system/korean/2.-setup-tools/3-sale-order-module/3.2-sales-price-list.md",
    ),
    (
        "smartbooks-erp-system/korean/2/3./3.3.md",
        "smartbooks-erp-system/korean/2.-setup-tools/3-sale-order-module/3.3-sales-quotation.md",
    ),
    (
        "smartbooks-erp-system/korean/2/3./3.4..md",
        "smartbooks-erp-system/korean/2.-setup-tools/3-sale-order-module/3.4-sales-order.md",
    ),
    (
        "smartbooks-erp-system/korean/2/3./3.5.md",
        "smartbooks-erp-system/korean/2.-setup-tools/3-sale-order-module/3.5-update-unit-price-so.md",
    ),
    (
        "smartbooks-erp-system/korean/2/3./3.6.md",
        "smartbooks-erp-system/korean/2.-setup-tools/3-sale-order-module/3.6-delivery-note.md",
    ),
    (
        "smartbooks-erp-system/korean/2/3./3.7.md",
        "smartbooks-erp-system/korean/2.-setup-tools/3-sale-order-module/3.7-sales-return.md",
    ),
    (
        "smartbooks-erp-system/korean/2/3./3.8.md",
        "smartbooks-erp-system/korean/2.-setup-tools/3-sale-order-module/3.8-matching-output-invoices.md",
    ),
    # 4. PURCHASE ORDER MODULE
    (
        "smartbooks-erp-system/korean/2/3./4./README.md",
        "smartbooks-erp-system/korean/2.-setup-tools/3-sale-order-module/4-purchase-order-module/README.md",
    ),
    (
        "smartbooks-erp-system/korean/2/3./4./4.1.md",
        "smartbooks-erp-system/korean/2.-setup-tools/3-sale-order-module/4-purchase-order-module/4.1-vendor-of-list.md",
    ),
    (
        "smartbooks-erp-system/korean/2/3./4./4.2.md",
        "smartbooks-erp-system/korean/2.-setup-tools/3-sale-order-module/4-purchase-order-module/4.2-vendor-price-list.md",
    ),
    (
        "smartbooks-erp-system/korean/2/3./4./4.3.md",
        "smartbooks-erp-system/korean/2.-setup-tools/3-sale-order-module/4-purchase-order-module/4.3-purchase-order.md",
    ),
    (
        "smartbooks-erp-system/korean/2/3./4./4.4-po.md",
        "smartbooks-erp-system/korean/2.-setup-tools/3-sale-order-module/4-purchase-order-module/4.4-update-unit-price-po.md",
    ),
    (
        "smartbooks-erp-system/korean/2/3./4./4.5..md",
        "smartbooks-erp-system/korean/2.-setup-tools/3-sale-order-module/4-purchase-order-module/4.5-receipt-note.md",
    ),
    (
        "smartbooks-erp-system/korean/2/3./4./4.6.md",
        "smartbooks-erp-system/korean/2.-setup-tools/3-sale-order-module/4-purchase-order-module/4.6-return-to-vendor.md",
    ),
    (
        "smartbooks-erp-system/korean/2/3./4./4.7.md",
        "smartbooks-erp-system/korean/2.-setup-tools/3-sale-order-module/4-purchase-order-module/4.7-update-of-input-invoices.md",
    ),
    # 5. MANUFACTURING MODULE
    (
        "smartbooks-erp-system/korean/2/3./4./5./README.md",
        "smartbooks-erp-system/korean/2.-setup-tools/3-sale-order-module/4-purchase-order-module/5-manufacturing-module/README.md",
    ),
    (
        "smartbooks-erp-system/korean/2/3./4./5./5.1-bom.md",
        "smartbooks-erp-system/korean/2.-setup-tools/3-sale-order-module/4-purchase-order-module/5-manufacturing-module/5.1-bom-list.md",
    ),
    (
        "smartbooks-erp-system/korean/2/3./4./5./5.2-mo.md",
        "smartbooks-erp-system/korean/2.-setup-tools/3-sale-order-module/4-purchase-order-module/5-manufacturing-module/5.2-manufacturing-order-mo.md",
    ),
    (
        "smartbooks-erp-system/korean/2/3./4./5./5.3.md",
        "smartbooks-erp-system/korean/2.-setup-tools/3-sale-order-module/4-purchase-order-module/5-manufacturing-module/5.3-finished-goods-receipt.md",
    ),
    (
        "smartbooks-erp-system/korean/2/3./4./5./5.4..md",
        "smartbooks-erp-system/korean/2.-setup-tools/3-sale-order-module/4-purchase-order-module/5-manufacturing-module/5.4-material-issue-note.md",
    ),
    # 6. INVENTORY MODULE
    (
        "smartbooks-erp-system/korean/2/3./4./5./6./README.md",
        "smartbooks-erp-system/korean/2.-setup-tools/3-sale-order-module/4-purchase-order-module/5-manufacturing-module/6-inventory-module/README.md",
    ),
    (
        "smartbooks-erp-system/korean/2/3./4./5./6./6.1.md",
        "smartbooks-erp-system/korean/2.-setup-tools/3-sale-order-module/4-purchase-order-module/5-manufacturing-module/6-inventory-module/6.1-item-list.md",
    ),
    (
        "smartbooks-erp-system/korean/2/3./4./5./6./6.2.md",
        "smartbooks-erp-system/korean/2.-setup-tools/3-sale-order-module/4-purchase-order-module/5-manufacturing-module/6-inventory-module/6.2-inventory-request-list.md",
    ),
    (
        "smartbooks-erp-system/korean/2/3./4./5./6./6.3-stock-transfer.md",
        "smartbooks-erp-system/korean/2.-setup-tools/3-sale-order-module/4-purchase-order-module/5-manufacturing-module/6-inventory-module/6.3-stock-transfer.md",
    ),
    (
        "smartbooks-erp-system/korean/2/3./4./5./6./6.4-stocktaking.md",
        "smartbooks-erp-system/korean/2.-setup-tools/3-sale-order-module/4-purchase-order-module/5-manufacturing-module/6-inventory-module/6.4-stocktaking.md",
    ),
    (
        "smartbooks-erp-system/korean/2/3./4./5./6./6.5-stock-adjustment.md",
        "smartbooks-erp-system/korean/2.-setup-tools/3-sale-order-module/4-purchase-order-module/5-manufacturing-module/6-inventory-module/6.5-stock-adjustment.md",
    ),
    (
        "smartbooks-erp-system/korean/2/3./4./5./6./6.6-other-input-output-inventory.md",
        "smartbooks-erp-system/korean/2.-setup-tools/3-sale-order-module/4-purchase-order-module/5-manufacturing-module/6-inventory-module/6.6-other-input-output-inventory.md",
    ),
    # 7. QUALITY CONTROL
    (
        "smartbooks-erp-system/korean/2/3./4./5./6./7./README.md",
        "smartbooks-erp-system/korean/2.-setup-tools/3-sale-order-module/4-purchase-order-module/5-manufacturing-module/6-inventory-module/7-quality-control/README.md",
    ),
    (
        "smartbooks-erp-system/korean/2/3./4./5./6./7./7.1-iqc.md",
        "smartbooks-erp-system/korean/2.-setup-tools/3-sale-order-module/4-purchase-order-module/5-manufacturing-module/6-inventory-module/7-quality-control/7.1-input-quality-control-iqc.md",
    ),
    (
        "smartbooks-erp-system/korean/2/3./4./5./6./7./7.2-oqc.md",
        "smartbooks-erp-system/korean/2.-setup-tools/3-sale-order-module/4-purchase-order-module/5-manufacturing-module/6-inventory-module/7-quality-control/7.2-output-quality-control-qoc.md",
    ),
]


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def is_windows_invalid(name: str) -> list[str]:
    """Return a list of reasons why *name* is Windows-incompatible, or []."""
    reasons: list[str] = []
    stem = name.rstrip("/")
    if stem.endswith(".") or stem.endswith(" "):
        reasons.append("trailing dot or space")
    if WIN_FORBIDDEN.search(stem):
        reasons.append("forbidden character")
    base = Path(stem).stem.upper()
    if base in RESERVED:
        reasons.append(f"reserved name ({base})")
    return reasons


def scan_invalid_paths(root: Path) -> list[tuple[Path, list[str]]]:
    """Walk *root* and return all paths with Windows-incompatible components."""
    bad: list[tuple[Path, list[str]]] = []
    for dirpath, dirnames, filenames in os.walk(root):
        dp = Path(dirpath)
        for entry in list(dirnames) + list(filenames):
            reasons = is_windows_invalid(entry)
            if reasons:
                bad.append((dp / entry, reasons))
    return bad


def verify_summary_links(summary_path: Path) -> list[str]:
    """Return a list of broken local Markdown links found in *summary_path*."""
    if not summary_path.exists():
        return [f"SUMMARY.md not found: {summary_path}"]
    base = summary_path.parent
    broken: list[str] = []
    link_re = re.compile(r'\[.*?\]\(([^)#]+?)(?:#[^)]*)?\)')
    for line in summary_path.read_text(encoding="utf-8").splitlines():
        for m in link_re.finditer(line):
            href = m.group(1)
            if href.startswith("http://") or href.startswith("https://"):
                continue
            target = (base / href).resolve()
            if not target.exists():
                broken.append(f"  BROKEN: {href!r}  (expected {target})")
    return broken


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    print("=" * 70)
    print("fix_gitbook_windows_paths.py — audit report")
    print("=" * 70)

    # 1. Scan for remaining Windows-invalid paths
    print("\n[1] Scanning for Windows-invalid paths …")
    invalid: list[tuple[Path, list[str]]] = []
    for project in PROJECTS:
        project_dir = REPO_ROOT / project
        if project_dir.is_dir():
            invalid.extend(scan_invalid_paths(project_dir))

    if invalid:
        print(f"  ✗ {len(invalid)} Windows-invalid path(s) found:")
        for path, reasons in invalid:
            rel = path.relative_to(REPO_ROOT)
            print(f"    {rel}  ← {', '.join(reasons)}")
    else:
        print("  ✓ No Windows-invalid paths found.")

    # 2. Print rename summary
    print(f"\n[2] Documented renames ({len(RENAMES)} total):")
    for old, new in RENAMES:
        old_exists = (REPO_ROOT / old).exists()
        new_exists = (REPO_ROOT / new).exists()
        status = "✓ applied" if (not old_exists and new_exists) else (
            "✗ old still present" if old_exists else "✗ new missing"
        )
        print(f"  [{status}]")
        print(f"    OLD: {old}")
        print(f"    NEW: {new}")

    # 3. Verify SUMMARY.md links
    print("\n[3] Verifying SUMMARY.md links …")
    all_broken: list[str] = []
    for project in PROJECTS:
        for lang in ("korean", "english", "vietnamese"):
            summary = REPO_ROOT / project / lang / "SUMMARY.md"
            broken = verify_summary_links(summary)
            if broken:
                all_broken.append(f"  {project}/{lang}/SUMMARY.md:")
                all_broken.extend(broken)

    if all_broken:
        print(f"  ✗ Broken links found:")
        for line in all_broken:
            print(line)
    else:
        print("  ✓ All SUMMARY.md links are valid.")

    ok = not invalid and not all_broken
    print("\n" + ("✓ All checks passed." if ok else "✗ Issues remain — see above."))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
