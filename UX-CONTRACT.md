# UX contract · Student Digital Profile

SDP-7 design handoff · Aimaut Bolatkhanuly (`aimautb`) · Updated 24 October 2026

This contract specifies future implementation behaviour. Figma demonstrates selected predefined states; it does not implement API requests, authorization, input validation or persistent storage.

## Canonical ownership

The revision 04 local preview retains a native HTML select for the reviewer-only screen chooser. Its platform popup, keyboard interaction and geometry are intentionally accepted; this is not the product's semester control. `docs/ux/figma-prototype/audit-config.json` records this native ownership for the preview scope. Plugin-panel buttons use explicit actions and disabled busy states. These utilities do not change the product's future runtime contracts below.

| Capability | Design owner | Future runtime owner | Verification |
| --- | --- | --- | --- |
| Buttons/navigation | Shared library instances with SDP overrides | Shared Button / navigation primitives | Pointer, keyboard, focus and selected states |
| Forms/errors | Label + field + inline error pattern | Shared Field and form validation adapter | Invalid submit, value retention, associated error |
| Semester selection | One period selector pattern | Shared native select, if platform-owned popup is accepted | Keyboard selection and chart/table synchronization |
| Dates | Labelled date field | Shared native date control, pending locale verification | Keyboard, locale and invalid input |
| Academic tables | Course-result table / mobile course cards | Semantic HTML table and responsive card view | Headers, order, overflow, equivalent values |
| Notifications | Persistent inline status / success view | Shared status/live-region provider | Save success/failure and announcement |
| Scrollbars | Visible native baseline | Global application stylesheet | Scroll, focus visibility, stable layout |
| Access restrictions | Source-defined ownership and assignment rules | Server authorization + route guards | Direct request tests; no data leak |

There is no existing application code or sibling implementation to reuse in this repository baseline. Do not create parallel per-screen primitives when implementation begins.

## Consistent operations

| Operation | Pending | Success | Failure / cancellation |
| --- | --- | --- | --- |
| Sign in | Preserve form size, prevent repeat submit | Role workspace | Generic error; no account enumeration |
| Change semester | Preserve panel dimensions; cancel stale request | Records and GPA update together | Preserve selected period; clear stale numeric claims; retry |
| Add achievement | Preserve inputs; save once | Return to owning list with new item and status | Keep inputs; inline error; cancel returns to list |
| Edit achievement | Keep ownership, date and evidence; validate title | Updated details and owning list | Original entry remains unchanged on validation failure or discard |
| Create profile | Validate required metadata and unique institutional ID | Restricted Student profile and updated account list | Reject duplicate ID; preserve existing accounts |
| Change role | Review old/new role and assigned-course scope explicitly | New role with its actual assignments only | Cancel preserves original metadata and role |
| Activate grading version | Validate range; preview calculation impact | New version without overwriting historical rules | Invalid points or discarded draft leave active version unchanged |
| Edit result | Validate role/scope and grade policy | Return to assigned list, restore filters, refresh indicators | Original record remains unchanged; conflict asks for reload/review |
| Revoke assignment | Review affected scope before committing | Subsequent requests use new scope | Keep original assignment on failed mutation |

Figma success views explain outcomes; runtime save flows should return to the owning list with inline feedback, instead of requiring an extra success page unless usability review supports it.

## Lists and request state

Use server pagination for the future teacher/admin directories. Preserve course, group, committed query, sort and page on return from details. Reset to page one after filter changes. Do not put student names, credentials or sensitive form data in URLs. A nonempty query needs a clear button. Debounce remote search by 300 ms, handle IME composition and ignore superseded responses. The current three-row Figma fixture is not a pagination implementation.

## Recovery and access

Differentiate no records, no search matches, unavailable service, expired session and denied access. Missing GPA is not zero. Keep form values on recoverable failure; do not display success before the backend confirms. Prevent duplicate saves. A chart cannot keep showing old values under a newly selected semester label.

Only authorized viewers may request profile data and attachments. Wider teacher visibility, adviser mapping, administrator grade edits, certificate retention/deletion and real upload policy remain unresolved requirements from SDP-5. The prototype must not be used as authorization policy.

## Accessibility and responsive acceptance

Target WCAG 2.2 AA in implementation: real links/buttons, visible focus, labels and error associations, non-colour statuses, password-manager support, keyboard-complete navigation and chart data alternatives. Document reading order and ensure phone cards retain all academic values. Test at 390/768/1440 px, with keyboard and 200% zoom. A Figma screenshot cannot establish these runtime properties.

## Deferred capabilities

Revision 04 demonstrates role changes, grading drafts and assignment removal using fictional, predefined states with explicit confirmations. Production rules, authorization, retention/deletion policies and import scope still require agreement before implementation. No real account, academic result, attachment or permission is changed by the prototype. Multilingual production copy, dark mode, external integrations and PDF export remain future scope.
