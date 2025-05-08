## Milestone 2 - Recipes
- Jesse Mendoza (@jesseemendozaa)
- Rustico Cruz (@Rooosti)
- Eric Lazarit-Orozco (@ericlazarit)

# Setup instructions:

<p>Clone repo<br>
Navigate to project folder</p>

from the parent folder, run in the terminal:
```
python3 -m venv venv
```
then:
```
source venv/bin/activate
```

after, install necessary libraries using pip3:
```
pip3 install -r requirements.txt
```

# Remember to stop VENV after running:
To stop the python virtual environment, run in the terminal:
```
deactivate
```

# Functional Requirements Implemented (7 or more):
<p>1. User Registration – The system shall allow users to register by providing a username, email, and password.</br>
IMPLEMENTED BY JESSE</br>
2. User Login – The system shall authenticate users based on their credentials to allow access.</br>
IMPLEMENTED BY RUSTICO</br>
3. User Logout – The system shall allow logged-in users to securely log out.</br>
IMPLEMENTED BY ERIC</br>
4. Create Recipe – The system shall allow users to create and submit new recipes with ingredients and instructions.</br>
ALREADY IMPLEMENTED</br>
5. Delete Recipe – The system shall allow users to delete their own submitted recipes.</br>
ALREADY IMPLEMENTED</br>
6. Save Recipe (Favorites) – The system shall allow users to save recipes to their favorites list.</br>
ALREADY IMPLEMENTED</br>
7. View All Recipes – The system shall allow users to view a list of all publicly available recipes.</br>
ALREADY IMPLEMENTED</p>

# To test functionality, please visit these endpoints and routes:
```
/login
/registration
/logout
/recipe/new
/recipe/<int>
/recipe/<int>/delete
/recipes
```
To test login, please use a test login profile:
Username: admin
Password: password
