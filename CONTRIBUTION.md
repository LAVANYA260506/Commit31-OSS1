**Contributing to our project**

First off, thank you for joining our Open Source event! Whether you’re fixing a typo or building a full feature, your contribution helps make this project better.
The "Vibe" & Design Language

To keep the app looking cohesive, we follow a Modern Linear aesthetic. Please stick to these guidelines when working on the frontend:

- Colors: Use a Slate/Off-white background (#F9FAFB) and Indigo (#6366F1) for primary actions.
- Corners: All buttons, cards, and inputs should have a border-radius of 8px.
- Simplicity: Favor whitespace and clear typography over heavy shadows or complex gradients.

**Getting Started**

- Find an Issue: Look for issues labeled good first issue or help wanted.
- Claim It: Comment on the issue so a maintainer can assign it to you. This prevents double-work!
- Fork & Clone: Fork the repo and create a new branch for your feature:
  git checkout -b feature/your-feature-name

**Technical Setup**

- Frontend: Navigate to /frontend, run npm install, then npm run dev.

- Backend: Navigate to /backend, create a virtual environment, run pip install -r requirements.txt, and start the server with uvicorn main:app --reload.

- Database: We use SQLite via SQLAlchemy. You don't need to install a DB server; the tasks.db file will be generated automatically on your first run.

**Contribution Guidelines**

1. **Small & Incremental**: We prefer small, focused Pull Requests (PRs). If an issue is too big, feel free to break it into two!

2. **Code Style**

- Frontend: Use functional components in React and descriptive variable names.

- Backend: Ensure all FastAPI routes use Pydantic schemas for request validation.

- Database: Use the get_db dependency to handle sessions, never leave a database connection hanging open.

3. New Issues

We will be assigning new sets of issues at regular intervals throughout the event. Once you finish a task and it’s merged, check back for the next "level" of challenges!

**Need Help?**

Stuck on an issue? Can’t get your CSS to align? Don't sweat it!

- Ping the Maintainers: Tag us in the comments of your issue or reach out on our community channel.

- Check the Docs: FastAPI’s /docs page (Swagger UI) is your best friend for testing endpoints.

📋 Pull Request Checklist

    [ ] My code follows the project's design language.

    [ ] I have tested my changes locally.

    [ ] My PR description clearly states which issue it fixes.

    [ ] (Backend) I have updated the Pydantic schemas if I changed the database model.


Happy Hacking! 
