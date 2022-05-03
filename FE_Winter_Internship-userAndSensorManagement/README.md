#FE User And Sensor Management System

Aim:

- To design and populate the sensor management and user management databases.

Tasks:

1. Sensor Management:

- Sensor Management Logic
- Design database schema and populate it with dummy data then real data of sensors in the cold rooms, pack house, pre-cooling, etc
- Show the table of sensors
- Implement Add, Remove, Edit, View operations
- Allow this functionality to allowed roles only
- Implement table filters as per need

2. User Management:

- User Register and Login System
- Employee CRUD
- FE User CRUD

Designed database for:

1. Master:

- CREATE TABLE master(
  id INT UNSIGNED NOT NULL AUTO_INCREMENT,
  siteLocation VARCHAR (20) NOT NULL,
  room VARCHAR (20) NOT NULL,
  masterName VARCHAR (20) NOT NULL,
  installationDatetime DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY(id)
  );

2. Sensor:

- CREATE TABLE sensor(
  id INT UNSIGNED NOT NULL AUTO_INCREMENT,
  masterId INT UNSIGNED NOT NULL,
  FOREIGN KEY (masterId) REFERENCES master(id) ON DELETE CASCADE,
  room VARCHAR (20) NOT NULL,
  sensorType VARCHAR (20) NOT NULL,
  compressor VARCHAR (20) NOT NULL,
  installationDatetime DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY(id)
  );

Database used: pipbiumy_fedbmiraj

Tables used in various functions:

1. Register and Login System:

- Three tables namely, 'auth_user', 'Login_appuser', and 'employee' are used as per requirement.
- For customized fields for user we have created 'Login_appuser' table, the 'user_id' attribute in 'Login_appuser' table stores the 'id' of the particular user from 'auth_user' table.
- For creating same user in 'system_users' table, username is used and a system user is created.


- 1. Register

  - For registering with the system, User can enter the desired username and his employee code on the landing page.
  - If entered data is true and verified, a user is created in 'auth_user' table, after user creation a loginappuser and systemuser is created in 'Login_appuser' and 'system_users' table, respectively.
  - Using employee code, an employee is extracted from 'employee' table and auto-generated Login credentials are generated, stored in 'auth_user' table and emailed to user's registered email ID.
  - Employee Code and User ID are stored in 'Login_appuser' table with associated 'user_id'.

- 2. Login

  - The emailed credentials ensure a successsful login.
  - The 'userCreated' attribute in 'employee' table for the corressponding employee code decides whether to send the user to New Password view or Dashboard view after successful login.
  - If the 'userCreated' attribute in 'employee' table for the corressponding employee code is '0' initially then it is set to '1' after successful login and the 'New Password' page is rendered to set a user desired password for the user.
  - Else if the 'userCreated' attribute is already '1' then the user is directly redirected to the Application's Dashboard.

- 3. New Password

  - Here the basic requirements for standard strong password are set and after validating them, the password is updated in 'auth_user' table.
  - The password updation acknowledgement is sent on the registered email extracted from the 'employee' teble for the current user.

- 4. Reset Password

  - Firstly user need to enter his/her username and employee code.
  - The system validates the username and employee code by fetching these values from 'Login_appuser' table and 'employee' table respectively else shows corressponding errors for correction.
  - If entered data is true and verified, a user is fetched from the 'auth_user' table using 'username' attribute.
  - Using employee code, an employee is extracted from 'employee' table and auto-generated Login credentials are generated, updated in 'auth_user' table and emailed to user's registered email ID.
  - The 'userCreated' attribute in 'employee' table for the corressponding employee code is set to '0'.
  - Hence redirecting back to Login page and successful login, the 'userCreated' attribute is 0 and hence system reditects a New Password view to the user.
  - Hence a password a reset sucessfully as mentioned in above New Passsword section.

- 5. User Profile

  - User can view and change his username and password from here.
  - Basic validations for strong standard passwords are applied as well as for non repetetive usernames too.
  - On updating username, it get's updated at 'username' attribute in 'auth_user' table as well as at 'u_username' attribute in system_users' table.
  - On updating password, it get's updated at 'password' attribute in 'auth_user' table.



2. Employee CRUD:

 - After login, the user management user has the authority to add, view, edit or deactivate an employee. The employee data will be added or modified in the table employee.
 - When user management user will add the employee details, all validations (employee must have unique empcode, valid aadhar number, valid account number, valid ifsc code, valid pan number, etc) will be checked and then only the employee data will be added in the system.
 - User management user can edit the employee details if required with proper validations mentioned above.
 - For inactivating an employee, user management user have to click on delete option and after clicking on it, the confirmation for inactivating an employee will be displayed and after clicking on YES option, the employee's activity status will set to inactive which will indicate that the employee is no more active in the companty.



3. FE User Team Allotment:
  
  - User management user will allot the teams and add the activity status to the register FE Users.
  - After team allotment, the FE User will get the access to the respective inputform tabs and other access options associated with the team and other remaining inputform tabs and other access options for that FE User will be denied. 
  - Multiple teams can be alloted to the same user.
  - User management user also can change the alloted teams of the registered FE Users.
  - For inactivating an FE User, user management user have to click on delete option and after clicking on it, the confirmation for inactivating an FE User will be displayed and after clicking on YES option, the FE User's activity status will set to inactive which will indicate that the FE User is no more active in the companty.
