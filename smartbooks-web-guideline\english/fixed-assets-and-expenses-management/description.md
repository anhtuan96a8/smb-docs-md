# 5.1 Master Data

The Fixed Assets module helps manage information on fixed assets and track their monthly depreciation and allocation.\
From the category table (Menu), the Fixed Assets module consists of five sections:

·       Master Data: List of Fixed Asset Group ID, List of Fixed Assets ID, List of Prepaid Expenses, Calculate Depreciation List, List of Allocation Expenses

·       Input: Fixed Asset Disposal, Fixed Asset Revaluation.

·       Proccess: Calculate Depreciation, Calculate Allocation Expense

·       Reports

<figure><img src="../.gitbook/assets/image (169).png" alt=""><figcaption></figcaption></figure>

### 5.1        Master Data

#### 5.1.1    List of Fixed Asset Group ID

The system classifies fixed assets and prepaid expenses into groups based on their management and usage purposes.

·       Group Code: Account group code

·       Description (VN, EN)

·       Account: Accounting account assigned to the classification group

<figure><img src="../.gitbook/assets/image (170).png" alt=""><figcaption></figcaption></figure>

#### 5.1.2    List of Fixed Assets ID

The Fixed Asset list manages all fixed assets within the company and is linked to the depreciation and disposal settings.

·       Asset ID: Input the fixed asset tracking code

·       Asset Name: Input name

·       History Cost

<figure><img src="../.gitbook/assets/image (171).png" alt=""><figcaption></figcaption></figure>

Number of months the asset has been in use.

·       Asset Group: Asset management group.

·       Unit

·       Purchase Date: Date the fixed asset was purchased

·       Quantity:

·       Months of depreciation: Estimated useful life in months.

·       Start Depreciation Date

·       End Depreciation Date

Used for cases where the fixed asset was already in use before being recorded in the software:

·       Last Depreciation Date: Date depreciation started

·       Last Depreciation Amount: Depreciation value recognized prior to system entry

·       Months of last depreciation: Number of months the asset has been in use.

<figure><img src="../.gitbook/assets/image (172).png" alt=""><figcaption></figcaption></figure>

In the **Account** section: detailed accounts used to record depreciation or gain/loss on disposal

·       Cost Account: ghi nhận tang giá trị TSCĐ

·       Acc. Dep. Account: ghi nhận tang giá trị khấu hao hàng kỳ

·       Revaluation Account: trường hợp TSCĐ được mua bằng tiền ngoại tệ

·       Profit on Sale Account/ Loss on Sale Account: trường hợp thanh lý TSCĐ

·       Expense Dep. Account: ghi nhận chi phí hàng kỳ

·       Rate (%) 1: tỷ lệ phân bổ chi phí khấu hao trường hợp TSCĐ dùng cho nhiều mục đích, bộ phận

·       Expense Dep. Account

·       Rate (%) 2

<figure><img src="../.gitbook/assets/image (173).png" alt=""><figcaption></figcaption></figure>

In the **Other Info: Detailed Information of Fixed Assets**

·       Label

·       Serial No.

·       Model

·       Original Country

·       Cost ID/ Profit ID/ JobCenter

<figure><img src="../.gitbook/assets/image (174).png" alt=""><figcaption></figcaption></figure>

#### 5.1.3    List of Prepaid Expenses

The Fixed Asset list manages all fixed assets within the company and is linked to the depreciation and disposal settings.

·       Tool ID: nhập mã theo dõi chi phí trả trước

·       Tool Name: nhập tên chi phí trả trước

·       Tool: giá trị theo hóa đơn

·       Quantity

<figure><img src="../.gitbook/assets/image (175).png" alt=""><figcaption></figcaption></figure>

In the **General Information** section: detailed information about prepaid expenses.

·       Allocate Time: thời gian phân bổ chi phí

·       Purchase Date: Ngày mua

·       Start Allocate Date

·       End Allocate Date

·       Cost ID/ Profit ID/ JobCenter

For cases where the expense had already been allocated before being entered into the system:

·       Allocated Time: Number of months already allocated.

·       Allocated Amount: Number of months already allocated.

·       Last Allocate Date: Number of months already allocated.

<figure><img src="../.gitbook/assets/image (176).png" alt=""><figcaption></figcaption></figure>

In the **Default** section: detailed accounts used to record prepaid expense allocations

·       Account: Records the prepaid amount.

·       Expense Dep. Account: Detailed account used to record allocated expenses

·       Rate (%) 1: Allocation rate for cases where the prepaid expense is used for multiple purposes or departments

·       Expense Dep. Account 2

·       Rate (%) 2

<figure><img src="../.gitbook/assets/image (177).png" alt=""><figcaption></figcaption></figure>

#### 5.1.4    Calculate Depreciation List

Calculate Depreciation List during the period from … to ….

<figure><img src="../.gitbook/assets/image (178).png" alt=""><figcaption></figcaption></figure>

To calculate automatic depreciation by period, select **Calculate Depreciation** to open the journal entry screen.

·       Voucher No: tự động theo số thứ tự

·       PO Date: ngày hạch toán

·       Period: lấy theo tháng hạch toán

·       Description VN/EN

Detailed fixed asset codes depreciated during the period are displayed in the data grid. Click **Save** to record the depreciation journal entry.

<figure><img src="../.gitbook/assets/image (179).png" alt=""><figcaption></figcaption></figure>

#### 5.1.5    List of Allocation Expenses

Similar to the Calculate Depreciation List, the **List of Allocation Expense** includes prepaid expenses that will be amortized during the period.

<figure><img src="../.gitbook/assets/image (147).png" alt=""><figcaption></figcaption></figure>

To calculate automatic allocation by period, select **Calculate Allocation Expense** to open the journal entry screen

·       Voucher No: Automatically generated in sequential order.

·       PO Date: Posting date

·       Period: Automatically assigned based on the posting month

·       Description VN/EN

Detailed prepaid expense codes for the period are displayed in the data grid. Click **Save** to record the allocation journal entry

<figure><img src="../.gitbook/assets/image (148).png" alt=""><figcaption></figcaption></figure>
