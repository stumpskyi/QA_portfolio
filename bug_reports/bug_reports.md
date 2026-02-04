**ID:** 1

**Title:** `[Security]` Lack of email validation during registration

**Severity:** Major

**Priority:** High

**Environment:** Windows 10 Pro 64-bit, Opera One 126.0.5750.59

### Test data
* **Email:** `bot_+%*@fake.email` 
* **Login:** `another_bot_account`
* **Password:** `whatever`

### Steps to reproduce
1. Navigate to `https://www.032.ua`;
2. Click on the **Profile icon** (top right corner) to open the registration form;
3. In the email input field, enter an email with a non-existent domain;
4. Fill in the name and password fields;
5. Click the **"Register"** button.

### Actual result
The account is created, and the user is successfully logged in. HTTP status code is `200 OK`. No email verification link is sent.

### Expected result
Registration should be rejected. The system should display the **"Enter a valid email address"** notification. Expected HTTP status code is `400 Bad Request`.

### Attachments
![email_validation_bug_1](https://github.com/user-attachments/assets/d2f21bcc-3260-4c60-be2b-add107aa8f12)
![email_validation_bug_2](https://github.com/user-attachments/assets/a4c49e3b-cd00-444f-869e-bff146928c3e)
![email_validation_bug_3](https://github.com/user-attachments/assets/9017c5e3-1ccd-463b-a3ec-12d5681f4e21)
![email_validation_bug_4](https://github.com/user-attachments/assets/e50cb9de-1c9f-4668-a443-5cebd4c4aac2)

_____________________________________________________________________________________________________________________________________________________________

**ID:** 2

**Title:** `[Security]` User profile picture accepts non-image files (no content type validation)

**Severity:** Critical

**Priority:** High

**Environment:** Windows 10 Pro 64-bit, Opera One 126.0.5750.59

### Preconditions
1. User should be logged in
2. A text file with changed format (txt -> jpg/png) is prepared
### Steps to reproduce
1. Click on the **Profile icon** (top right corner);
2. Click the **"Choose a photo"** button in the **Profile picture** section;
3. Choose the prepared file;
4. Click the **"Save changes"** button.

### Actual result
The file is accepted without any verification; profile picture render is failed - a distorted black image is shown instead. HTTP status code is 200 OK.

### Expected result
Uploading the file should be rejected with the "Invalid format. Only .jpg and .png file formats are supported." notification. Expected HTTP status code is 400 Bad Request.

### Attachments
![profile_picture_bug_1](https://github.com/user-attachments/assets/39f407fa-e631-4b7d-96e6-fa1b5130224e)
![profile_picture_bug_2](https://github.com/user-attachments/assets/8186fb30-3f88-4870-b4ca-0d895aa86adb)
