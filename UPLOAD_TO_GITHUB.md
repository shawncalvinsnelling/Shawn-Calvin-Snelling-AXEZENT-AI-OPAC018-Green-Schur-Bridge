# Upload to GitHub - Clean Reset Instructions

## Safer recommendation

Do **not** delete the old repository until you have downloaded a backup of:

- old source ZIPs;
- releases;
- receipts;
- issue/comments history;
- PDFs.

If you want a clean history, the safest path is:

```text
1. Create a new repository with a clean name, or archive the old repo.
2. Upload this package as the first commit.
3. Confirm Actions are green.
4. Enable GitHub Pages.
```

## If you still want to delete and recreate

1. Download this ZIP and keep a backup.
2. Delete the old GitHub repository only after backup.
3. Create a new public repo with the same name.
4. Drag all extracted files into the new repo root.
5. Commit:

```text
Clean referee reset v1.5.0
```

6. Wait for Actions:

```text
Manifest Check
Pure Python Exact Audit
Counterexample Stress Test
```

7. Manually run:

```text
Sage Exact Audit Manual
```

8. Create release:

```text
v1.5.0 Clean Referee Reset
```

## GitHub Pages website

Settings -> Pages -> Build and deployment -> Deploy from a branch.

Set:

```text
Branch: main
Folder: /root
```

The site will use:

```text
index.html
assets/site.css
```
