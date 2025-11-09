# Specifications

This directory contains feature specifications following a structured naming convention and template.

## Directory Structure

```
specs/
├── README.md          # This file - naming conventions and guidelines
├── TEMPLATE.md        # Template for new specifications
├── implemented/       # Completed and implemented features
│   ├── app-backend-api.md
│   ├── app-frontend-html-integration.md
│   ├── package-pdf-reader.md
│   └── package-xlsx-reader.md
└── planned/          # Future features not yet implemented
```

---

## Naming Convention

All specification files must follow this naming pattern:

```
<type>-<scope>-<feature>.md
```

### Type Prefix

| Prefix | Description | Example |
|--------|-------------|---------|
| `package-` | Standalone package in `packages/` | `package-pdf-reader.md` |
| `app-` | Application in `apps/` | `app-backend-api.md` |
| `feature-` | Cross-cutting feature | `feature-authentication.md` |
| `integration-` | Integration between components | `integration-backend-frontend.md` |
| `infrastructure-` | Infrastructure or tooling | `infrastructure-ci-cd.md` |

### Scope

For apps, include the app name:
- `app-backend-*` - Backend application features
- `app-frontend-*` - Frontend application features

For packages, include the package name:
- `package-pdf-reader-*` - PDF reader package
- `package-xlsx-reader-*` - XLSX reader package

### Feature Name

Use kebab-case for the feature description:
- Single word: `api`, `authentication`, `validation`
- Multiple words: `html-integration`, `user-management`, `error-handling`

---

## Naming Examples

### Packages
```
package-pdf-reader.md              # The PDF reader package itself
package-pdf-reader-encryption.md   # Add encryption support to PDF reader
package-csv-reader.md              # New CSV reader package
package-xlsx-reader-formulas.md    # Add formula support to XLSX reader
```

### Applications
```
app-backend-api.md                 # The backend API application
app-backend-authentication.md      # Add auth to backend
app-backend-rate-limiting.md       # Add rate limiting to backend
app-frontend-html-integration.md   # HTML integration for frontend
app-frontend-dark-mode.md          # Add dark mode to frontend
```

### Features (Cross-Cutting)
```
feature-authentication.md          # Auth across all apps
feature-logging.md                 # Logging infrastructure
feature-error-handling.md          # Error handling standards
```

### Integrations
```
integration-backend-frontend.md    # Backend-frontend integration
integration-pdf-api.md             # PDF reader API endpoint integration
```

### Infrastructure
```
infrastructure-ci-cd.md            # CI/CD pipeline
infrastructure-docker.md           # Docker setup
infrastructure-monitoring.md       # Monitoring and observability
```

---

## Spec Lifecycle

### 1. Planning Phase
- File location: `specs/planned/`
- Status in file: `**Status:** 📋 Planned`
- Use the [TEMPLATE.md](TEMPLATE.md) to create new specs

### 2. Implementation Phase
- File stays in: `specs/planned/`
- Status in file: `**Status:** 🚧 In Progress`
- Update as you implement

### 3. Completion Phase
- Move to: `specs/implemented/`
- Status in file: `**Status:** ✅ Implemented`
- Add implementation details (version, location, date)

---

## Creating a New Spec

### Step 1: Choose the Right Type

**Is it a new package?**
→ Use `package-<name>.md`

**Is it a feature for an existing app?**
→ Use `app-<app-name>-<feature>.md`

**Does it span multiple components?**
→ Use `feature-<name>.md` or `integration-<name>.md`

**Is it infrastructure?**
→ Use `infrastructure-<name>.md`

### Step 2: Copy the Template

```bash
cp specs/TEMPLATE.md specs/planned/<type>-<scope>-<feature>.md
```

### Step 3: Fill in the Template

- Update the title
- Fill in all sections
- Set status to 📋 Planned
- Be specific and thorough

### Step 4: Implement

Follow the spec-driven development workflow:
1. Review and refine the spec
2. Implement according to spec
3. Write tests
4. Verify all requirements met

### Step 5: Mark as Implemented

```bash
# Move to implemented
git mv specs/planned/<name>.md specs/implemented/<name>.md

# Update status in file
# Status: ✅ Implemented
# Implemented: YYYY-MM-DD
# Version: X.Y.Z
# Location: path/to/implementation
```

---

## Spec Template Structure

Every spec should include:

1. **Header**
   - Title
   - Status
   - Type
   - Implementation details (if implemented)

2. **Overview**
   - What is this feature?
   - Why do we need it?
   - Who is it for?

3. **Requirements**
   - Functional Requirements (FR)
   - Non-Functional Requirements (NFR)
   - Constraints

4. **Design**
   - API design
   - Data models
   - Architecture decisions

5. **Implementation**
   - Dependencies
   - File structure
   - Key components

6. **Testing**
   - Test strategy
   - Test cases
   - Acceptance criteria

7. **Documentation**
   - User documentation
   - Developer documentation
   - Examples

See [TEMPLATE.md](TEMPLATE.md) for the complete template.

---

## Quick Reference

### Current Specs

**Implemented (4):**
- [package-pdf-reader.md](implemented/package-pdf-reader.md) - PDF text extraction
- [package-xlsx-reader.md](implemented/package-xlsx-reader.md) - Excel data extraction
- [app-backend-api.md](implemented/app-backend-api.md) - FastAPI REST API
- [app-frontend-html-integration.md](implemented/app-frontend-html-integration.md) - Static HTML frontend

**Planned (0):**
- None currently

### Example Prompts

**Create a new package spec:**
```
Write a specification for a CSV reader package.
Use the template from specs/TEMPLATE.md
Save it as specs/planned/package-csv-reader.md
```

**Create an app feature spec:**
```
Write a spec for adding authentication to the backend.
Save it as specs/planned/app-backend-authentication.md
Follow the template structure.
```

**Implement from spec:**
```
Implement the feature described in specs/planned/package-csv-reader.md
Follow the spec exactly.
```

**Mark as implemented:**
```
Move specs/planned/package-csv-reader.md to specs/implemented/
Update the status to ✅ Implemented
Add implementation date and location
```

---

## Best Practices

### DO

✅ **Use the template** - Ensures consistency
✅ **Be specific** - Clear requirements prevent ambiguity
✅ **Include examples** - Show what you mean
✅ **Define acceptance criteria** - Know when you're done
✅ **Update as you learn** - Specs can evolve during implementation
✅ **Move to implemented/** - Track what's completed

### DON'T

❌ **Skip the spec for complex features** - You'll regret it
❌ **Leave specs in planned/** after implementation - Move them!
❌ **Write vague requirements** - "Make it work" isn't a requirement
❌ **Forget to update status** - Keep the status current
❌ **Ignore the naming convention** - It provides structure

---

## Migration from Old Naming

If you have specs with old names, rename them:

```bash
# Old naming (bad)
specs/implemented/pdf-reader.md
specs/implemented/backend.md

# New naming (good)
specs/implemented/package-pdf-reader.md
specs/implemented/app-backend-api.md

# Rename
git mv specs/implemented/old-name.md specs/implemented/new-name.md
```

---

## See Also

- [TEMPLATE.md](TEMPLATE.md) - Specification template
- [Workflow Examples](../examples/) - How to use specs in workflows
- [Spec-Driven Development Example](../examples/01-spec-driven-development/) - Complete workflow
- [Documentation](../docs/workflows.md) - Development workflows
