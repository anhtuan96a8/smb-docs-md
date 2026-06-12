# Instructions to Get Data from Timekeeping Machine

## **Function description**

This function uses to get data of the start and end time of the shift of each employee from the timekeeper. Also, it can add timekeeping data in case of missing data.

## **Implementation instructions**

In the Task bar, choosing ![](<../.gitbook/assets/0 (122).png>) -> the interface will display two main tabs: General Tab and Delete List Tab.

### **General Tab**

![](<../.gitbook/assets/1 (162).png>)

VI.3.1

#### **Instructions to get timekeeping data: there are 2 methods**

* **Method 1**: Get data for all employees. Follow the instructions in the Figure VI.3.2

![](<../.gitbook/assets/2 (45).png>)

VI.3.2

Step 1: In the Function box, choose “Get timekeeping data”.

Step 2: Click Implement button.

Step 3: Select the data by filter available, there are filter by location and by time.

Step 4: Click the OK button to get data or click Cancel button to cancel.

* **Method 2**: Get data according to employee code. Follow the instructions in the Figure VI.3.3

![](<../.gitbook/assets/3 (51).png>)

VI.3.3

Step 1: In the Function box, choose “Get timekeeping according to employee code”.

Step 2: Click Implement button.

Step 3: Select the period to get data.

Step 4: Click OK button. Then the interface will display as Figure VI.3.4

![](<../.gitbook/assets/4 (27).png>)

VI.3.4

Step 5: Select the employee to get timekeeping data.

Step 6: Click the OK button to implement or click Cancel button to cancel.

#### **Additional guidance for timekeeping information for employees**

Implement same as the instructions in the section **II.2**

* Date, Time: is the date and time add to the timekeeping.
* In/out: the status of the time in/ time out.
* Reason: This is the reason for adding time in / time out.

#### **Instructions to edit, delete and export data**

To edit, delete and export data to Excel file, follow the instructions in the section **II.3, II.4, II.5, II.6.**

1. **Reports explanation**

* Timekeeping list by the shift registration: A list of employees had timekeeping data in accordance with the registered shift.
* List without timekeeping data by the shift registration: A list of employees who have registered shift but no timekeeping data.

### **Delete List Tab**

This Delete List tab storing the timekeeping data were deleted in the "General Tab" by users.

**Noted:** When retrieving timekeeping data from the timekeeper, the Smartbook software will not retrieve the employee data that the user has previously deleted.

1. **Instructions to edit, delete and export data**

To edit, delete and export data to Excel file, follow the instructions in the section **II.3, II.4, II.5, II.6.**
