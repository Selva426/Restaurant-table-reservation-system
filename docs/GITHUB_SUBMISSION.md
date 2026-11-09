# GitHub Submission

The project is published at https://github.com/Selva426/Restaurant-table-reservation-system. The repository includes the source code, migrations, tests, documentation, and screenshots.

To publish later updates, open PowerShell in the project folder and run:

```powershell
git add .
git status
git commit -m "Describe my project update"
git push
```

Before committing, confirm that `.env` is ignored and not staged. Commit `.env.example` with placeholders, never real credentials. Django settings read the database credentials and secret key from the local `.env` file.

Never commit `.env`, database passwords, production secret keys, or private customer information. If a credential is accidentally published, rotate it; deleting it from the latest version does not remove it from Git history.
