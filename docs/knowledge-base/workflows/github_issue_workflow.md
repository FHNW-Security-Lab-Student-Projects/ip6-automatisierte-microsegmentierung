# Git Workflow for Issues

This repository uses a **feature branch + pull request workflow**.

------------------------------------------------------------------------

## 1. Update `main`

Start from the latest version of the repository.

``` bash
git checkout main
git pull origin main
```

------------------------------------------------------------------------

## 2. Create a Feature Branch

Create a branch for the issue.

Branch naming:

    feature/<issue-number>-<short-description>

Example for issue `#1`:

``` bash
git checkout -b feature/1-project-structure
```

------------------------------------------------------------------------

## 3. Implement Changes

Make the required code or structure changes.

Stage all changes:

``` bash
git add .
```

------------------------------------------------------------------------

## 4. Commit and Link the Issue

Commit the changes and reference the issue so it closes automatically
when merged.

``` bash
git commit -m "Short description of change

Closes #<issue-number>"
```

Example:

``` bash
git commit -m "Create initial prototype project structure

Closes #1"
```

------------------------------------------------------------------------

## 5. Push the Branch

``` bash
git push -u origin feature/<issue-number>-<short-description>
```

Example:

``` bash
git push -u origin feature/1-project-structure
```

------------------------------------------------------------------------

## 6. Create a Pull Request

Use the GitHub CLI:

``` bash
gh pr create --fill
```

The PR will include the commit message referencing the issue.

------------------------------------------------------------------------

## 7. Merge the Pull Request

After review (or directly if working solo):

``` bash
gh pr merge --merge --delete-branch
```

This will:

-   merge the branch into `main`
-   delete the feature branch
-   automatically close the referenced issue

------------------------------------------------------------------------

## 8. Update Local Repository

``` bash
git checkout main
git pull origin main
```

------------------------------------------------------------------------

## Workflow Summary

    Issue → Feature Branch → Commit (Closes #X) → Pull Request → Merge → Issue Closed
