# GitHub Submission Guide

1. Create a new repository on GitHub named `restaurant-table-reservation-system`.
2. Keep it Public if your institute requires a public repository. Do not add a README on GitHub if you already have one locally.
3. In PowerShell, move into this project folder and run:

```powershell
git init
git add .
git status
```

4. Before staging files, confirm your local `.env` file is ignored and not staged. Commit `.env.example` only; it must contain placeholders, never real credentials. The Django settings read database credentials and the secret key from `.env`.
5. Commit and connect the repository (replace the URL with your own GitHub repository URL):

```powershell
git commit -m "Initial commit: Restaurant Table Reservation System"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/restaurant-table-reservation-system.git
git push -u origin main
```

6. Copy your actual GitHub repository URL into your submission document.
7. Add your application screenshots to a `screenshots/` folder and commit them:

```powershell
git add screenshots/
git commit -m "Add project screenshots"
git push
```

Never commit `.env`, database passwords, production secret keys, or private customer information. If a credential was committed earlier, rotate it; deleting it from the latest version does not remove it from Git history.
