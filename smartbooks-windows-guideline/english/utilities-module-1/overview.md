# 13.1 Approval System

<figure><img src="https://lh7-us.googleusercontent.com/ANej-KE0UNRcCK9_ovyclX9uLUq82odL2XrDRPyhpU_bWoY26zXQP1kgsYlZ5FsRrD7lNVx6h0H0xfiyqb18tq32iXVf3vLiz9QxDEPY811W70U85E-W1d2rqJGirmF6tuUuDC_a_gE2lq5DrLIFRsMKC5OyXo7z" alt=""><figcaption></figcaption></figure>

Approval System consists of 2 parts: Approval system and Report

**Approval System**

<figure><img src="../.gitbook/assets/image (43).png" alt=""><figcaption></figcaption></figure>

## This part contains six modules :

* Set up approval steps
* Payment request
* Payment approval
* Cashier’s book at beginning period&#x20;
* Awaiting payment
* Cashier collects money

### 13.1.1 Set up approval steps (For administrator):&#x20;

default setting for user (requester) who creates requests for payment&#x20;

Example: if you want members in your group (Employee A) before sending a payment request, he/she needs to send it to the group leader first, then the setup is as follows:

* Select user Employee A (optional) with highest priority
* Groups with low priority level.
* Group (optional)
* Expense items (optional)
* Profit centers (optional)

If you do not enter anything, the default is applied for everyone

<figure><img src="../.gitbook/assets/image (44).png" alt=""><figcaption></figcaption></figure>

<figure><img src="https://lh7-us.googleusercontent.com/WPQHpcgpVhuYPYOIAwJ40wnW7pjnB3FIrqy0pxig5oeeqEilM4neRkr1DqF7L6qUnfJ9uZmKKLshfH5nhr0KWLbn9Vqlq9A-YUEEW2rH5OIGkxRoCrkZIifKOo7dwsGYLqXk0UiyCkLqW6geFoTRw7gizg8UpBTH" alt=""><figcaption></figcaption></figure>

### 13.1.2 Payment request

<figure><img src="https://lh7-us.googleusercontent.com/7oi2FfOSHr1vQ_fXisRnKzW0Iqs7fiS3SYGV0Lgz592YxoaqHn1Sxe6rAl9IhodOAh7zwoHJ7rOQWZKLgR_KHclaSzqXjK1D6JQZx2eiz2adMGPyFEXx_giOMC5DjfkF1vapuRlcLSqsXRtyllZbnHzDFvgNUh0a" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (45).png" alt=""><figcaption></figcaption></figure>

This screen allows requester to manage his/her requisition with the status of each form, including:&#x20;

* Wait request – the form recently created and sent (not yet obtain any settlement from Approver)
* Wait Approve – there is at least one person approve this form
* Payable – complete approval process and proceed payment
* Finished – receipt money and finish the process
* Reject – for case Approver reject a request

And requester is able to manage his/her requisition by period from date to date.

Add new

### Click into Add new to fill out information of the approval request.&#x20;

<figure><img src="../.gitbook/assets/image (46).png" alt=""><figcaption></figcaption></figure>

<figure><img src="https://lh7-us.googleusercontent.com/ZtLy4Su0BLf320wwN0ayCK5DC1ZNEC4TA96GUalFSNgkgOT9vEoi4G01_bcaWGZpOrBaHyev1CzU0zkvm5MUaS1z-ZhT4nzApoNjtBA84Zke0EZxSqBuqD7Nrchj4ZczKIKf7iAc5I8iAR_bSTKGaqjPEvT3MgAr" alt=""><figcaption></figcaption></figure>

### The screen will pop out a window. Fill out the mandatory content as follows:

* Payment amount
* Currency ID in VND or in foreign currency USD, EUR, …
* Payment subject and payment explanation for Approver’s reference.&#x20;
* Approval information: Select ID of Approver, Approver name, Approver position is checked by whom, confirmed by whom, approved by whom. Each ID would let people choose a function to perform.&#x20;

### Optional filling:

* File attachment: Click into Browse to load word file, pdf, picture file or excel file,…

Once complete filling Approval information, click Save button.

At this point, the first control table displays approval status as follows:&#x20;

* Payment request status
* Payment approval status
* Payment approval complete status

### 13.1.3 Payment approval

<figure><img src="https://lh7-us.googleusercontent.com/u0p1BlAhk8ON_V0JIGvQPyWP7QM3Oehz0wq4WBqLDJ6TSCnpZuysZ_ZJTD4A26FBHZbnZROXO_h_ef9AaM5B815klfr0SbB-rboVOFnSyiHEN7MTeRTOsPNY-x6DK-3a2aleNKG6OFN95tQ0ZzrIo2braFJMO3MM" alt=""><figcaption></figcaption></figure>

Person who in charge of payment approval would view this area to get user (approver) support in searching for a list of request forms under 3 status, including:&#x20;

* Approval-awaiting form (wait)
* Approval-accepted form (accepted)
* Approval-rejected form (rejected)

And by period from date to date

Approver simply double click on the item, a detail screen will display approval content.

&#x20;

<figure><img src="https://lh7-us.googleusercontent.com/Ary4RdzIu9E0LJZCPQiCo1T93pVDy8Olg43WfLZKtfQsQBQuaYuTmai5G9OeEIzquis-p9p8BOki5Lz1w29IVquFeKI1mvbE3FlL_QS6yblL29lWr3ZYbMLsXkKzaIKN3Zp2CdS0d_b8ndfsxBUz0_DC6ixGrufM" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (48).png" alt=""><figcaption></figcaption></figure>

This window allows Approver to make decision on payment approval, there are 3 status including:&#x20;

* Wait: pending (no decision made)
* Accept: when a form is accepted, it will be transferred to the next approver, if the last approver accepted, the form will be in Payable status.
* Reject: dismiss a request with a description, the requester needs to correct the request and send it again.&#x20;

### 13.1.4 Awaiting payment

Awaiting payment screen allows cashier seeking payment request under 2 status including:&#x20;

* Payment-awaiting command&#x20;
* Payment-completed command&#x20;

And it support to search by period including 2 date types:

* Request form-sending date
* Request form-settlement date

Steps:&#x20;

* Click into finished-payment-standby status (finished)
* Select from date … to date …
* Click View or export into excel file

Double click to view payment details&#x20;

<figure><img src="../.gitbook/assets/image (49).png" alt=""><figcaption></figcaption></figure>

<figure><img src="https://lh7-us.googleusercontent.com/btyq9uM_Q8rVhd34r_Ot4iva0tjxOIrGQ4976CZBL-uJXqsw7Qn3poS9yajA4bDwLWgS5fb_1-eZ3thtxqINwaZLRMRpXhp1cO0_n47TerQCJ0cGovzmMjfyIbpbSjDLnamlNxuPmB9pe5B2_fqt3Ykl4mOY5sHA" alt=""><figcaption></figcaption></figure>

On this screen, cashier enters actual payment amount:&#x20;

* If  same currency, cashier is allowed to enter amount lesser or equal&#x20;
* If different currency, there is not a need to check the amount&#x20;
* Enter the remaining information if necessary
* Click into processing payment to create payment voucher

<figure><img src="../.gitbook/assets/image (50).png" alt=""><figcaption></figcaption></figure>



<figure><img src="https://lh7-us.googleusercontent.com/hhQkj8jIQA-OmCzHabiGe2qXAP9o857zY-qV9FnCgfaZLabjfJTBGXlIQOWPAV59jy_Uw6QqozephrS0HiGqpp6PNyKUaupif_0CxC-X4LnnB854yG7v1CuG0QjeHDXR-PoD2FfZC_QhpLc6NQaUG6OcteLBijV6" alt=""><figcaption></figcaption></figure>

Click Print to issue printing version and print out into paper to sign.

Payment voucher shows payment date

Recipient’s name, address

Payment reason

Payment amount

<figure><img src="../.gitbook/assets/image (51).png" alt=""><figcaption></figcaption></figure>

<figure><img src="https://lh7-us.googleusercontent.com/yrobXNhuYLYEq1yuw0LZX5LVtngnoLX0arpsW_nc1Bfpz0hhLm0D31FBSbAy_us6nYYMVYJUO8cqD0liIc7k7q_glxJjQkonl4HBZEy7hfrZT6PvDLXweE4M_aiT1lZzVrhzePzLmBXbyEo1iibOE7k4PMCjabw1" alt=""><figcaption></figcaption></figure>

This payment voucher also shows recipient signature, signed date. Approver’s signature, approval date.

Manager’s name, signature and signed date.

###

