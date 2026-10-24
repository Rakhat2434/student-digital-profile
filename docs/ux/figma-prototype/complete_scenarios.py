"""Revision 04: explicit achievement and administrator demonstration states.

These are fictional, predetermined states, not changes to accounts or policy.
"""


def extend(screens, d, base, panel, action, link, finish):
    C = d.C

    def form(key, title, fields, save, cancel, role='Administrator', error=None,
             note='Preset values only. No real records are changed.', extras=()):
        active = 'Achievements' if role == 'Student' else 'Assignments' if key.startswith('admin-assignment') else 'Grading policy' if key.startswith('admin-grading') else 'Accounts'
        b, s = base(key, title, active, role)
        b.rect(272, 224, 750, 682, C['white'], 12, C['line'])
        b.heading(300, 266, title, 22)
        for i, (label, value, target) in enumerate(fields):
            y = 298 + i * 84
            b.text(300, y, label, 13, C['ink'], 600)
            b.rect(300, y + 12, 694, 48, C['bg'], 8,
                   C['red'] if error and i == 0 else C['line'])
            b.text(316, y + 43, value, 15, C['ink'])
            if target:
                link(s, 300, y + 12, 694, 48, 'Choose ' + label, target)
        if error:
            for i, line in enumerate(error):
                b.text(300, 672 + i * 24, line, 14, C['red'])
        b.text(300, 745, 'Demo only · Review changes before saving.', 13, C['muted'])
        if save == key:
            b.text(300, 822, 'Correct the highlighted field first.', 13, C['red'])
        else:
            action(b, s, 300, 794, 'Review and save', save, 220, True)
        action(b, s, 544, 794, 'Cancel', cancel, 150)
        b.rect(1046, 224, 354, 440, C['soft'], 12)
        b.heading(1070, 270, 'Before you continue', 19)
        for i, line in enumerate(note.split('\n')):
            b.text(1070, 307 + i * 26, line, 13, C['muted'])
        for i, (label, target) in enumerate(extras):
            action(b, s, 1070, 454 + i * 64, label, target, 304)
        finish(s, b)
        return s

    # Edit an achievement which already exists before the add flow.
    research = screens['research']
    b, s = base('research', 'Research presentation', 'Achievements')
    b.rect(272, 224, 1128, 480, C['white'], 12, C['line'])
    b.heading(304, 280, 'Research presentation', 26)
    for i, text in enumerate(['Academic achievement · 23 October 2026',
                              'Presented a student research poster.',
                              'Evidence: sample-research.pdf · Fictional record']):
        b.text(304, 330 + i * 32, text, 16, C['muted'])
    for x, label, target in [(304, 'Edit achievement', 'edit-achievement'),
                              (568, 'View evidence', 'research-evidence'),
                              (832, 'Back to achievements', 'achievements')]:
        action(b, s, x, 534, label, target, 240, x == 304)
    finish(s, b)
    for key, title, value, error in [
        ('edit-achievement', 'Edit achievement', 'Research presentation', None),
        ('edit-achievement-error', 'Edit achievement', '(empty title)',
         ['A title is required. The existing record is unchanged.']),
        ('edit-achievement-ready', 'Edit achievement', 'Research poster presentation', None),
    ]:
        ready = key == 'edit-achievement-ready'
        form(key, title, [('Title', value, 'edit-achievement-ready'),
                         ('Category', 'Academic achievement', None),
                         ('Date', '23 October 2026', None),
                         ('Description', 'Presented a student research poster.', None)],
             'edit-achievement-saved' if ready else 'edit-achievement-error',
             'edit-achievement-discard', role='Student', error=error,
             note='Edit your own achievement.\nCertificate remains attached.\nInstitutional fields stay protected.',
             extras=[('Use revised sample', 'edit-achievement-ready'),
                     ('Test empty title', 'edit-achievement-error')])
    panel('edit-achievement-discard', 'Discard achievement edits?',
          ['The original research record remains unchanged until Save.',
           'Keep editing or return to the original details.'],
          [('Keep editing', 'edit-achievement-ready'), ('Discard edits', 'research')],
          active='Achievements')
    panel('edit-achievement-saved', 'Achievement changes saved',
          ['Research poster presentation · Academic achievement',
           'Date and attached certificate were preserved.',
           'Only the selected fictional achievement was changed.'],
          [('View updated details', 'research-updated'), ('View updated list', 'achievements-updated')],
          active='Achievements')
    panel('research-updated', 'Research poster presentation',
          ['Academic achievement · 23 October 2026',
           'Presented a student research poster.', 'Evidence: sample-research.pdf'],
          [('View updated list', 'achievements-updated'), ('Edit again', 'edit-achievement-ready')],
          active='Achievements')
    b, s = base('achievements-updated', 'Your achievements', 'Achievements')
    b.rect(272, 224, 1128, 390, C['white'], 12, C['line'])
    for i, (title, target) in enumerate([('Database design workshop', 'certificate'),
                                       ('Research poster presentation', 'research-updated')]):
        y = 270 + i * 126
        b.heading(300, y + 28, title, 23)
        b.text(300, y + 59, 'Evidence attached · Fictional record', 14, C['muted'])
        action(b, s, 1150, y + 12, 'View details', target, 220)
    b.text(300, 562, 'Updated title is reflected in this saved-list state.', 14, C['green'])
    finish(s, b)

    # Accounts and protected profile metadata: create, validate, edit and review role.
    for key, created in [('admin', False), ('admin-accounts-saved', True)]:
        b, s = base(key, 'Accounts and profiles', 'Accounts', 'Administrator')
        b.rect(272, 224, 1128, 586, C['white'], 12, C['line'])
        b.heading(300, 272, 'Demonstration accounts', 23)
        rows = [('Dana Sarsen', 'Student · DEMO-001 · SE-DEMO'),
                ('Teacher Demo', 'Teacher · Assigned courses only'),
                ('Admin Demo', 'Administrator · Configuration only')]
        if created:
            rows.append(('Mira Demo', 'Student · DEMO-004 · SE-DEMO'))
        for i, (name, context) in enumerate(rows):
            y = 304 + i * 96
            b.line(300, y + 84, 1372, y + 84)
            b.heading(300, y + 30, name, 20)
            b.text(300, y + 58, context, 14, C['muted'])
            if i == 0 or (created and i == 3):
                action(b, s, 1146, y + 14, 'Manage profile',
                       'admin-account-detail' if i == 0 else 'admin-created-detail', 224)
        action(b, s, 300, 738, 'Create student profile', 'admin-create', 250, True)
        finish(s, b)
    panel('admin-account-detail', 'Dana Sarsen · Account details',
          ['Institutional ID: DEMO-001 · Group: SE-DEMO',
           'Role: Student · Active account · Own records only',
           'Academic results are maintained by assigned teachers.',
           'No password or real personal data is displayed.'],
          [('Edit metadata / role', 'admin-edit'), ('Back to accounts', 'admin')],
          active='Accounts', role='Administrator')
    for key, filled, message in [
        ('admin-create', False, None),
        ('admin-create-error', False, ['Name and a unique institutional ID are required.']),
        ('admin-create-duplicate', True, ['DEMO-001 already exists. No account was created.',
                                        'Use DEMO-004 for the demonstration.']),
        ('admin-create-ready', True, None),
    ]:
        duplicate = key == 'admin-create-duplicate'
        form(key, 'Create student profile',
             [('Name', 'Mira Demo' if filled else '(required)', 'admin-create-ready'),
              ('Institutional ID', 'DEMO-001' if duplicate else 'DEMO-004' if filled else '(required)', 'admin-create-ready'),
              ('Group / programme', 'SE-DEMO / Software Engineering', 'admin-create-ready'),
              ('Role', 'Student · Own records only', None)],
             'admin-create-saved' if key == 'admin-create-ready' else key if duplicate else 'admin-create-error',
             'admin-create-discard', error=message,
             note='A unique ID identifies the profile.\nNo password is exposed or stored.\nOnly demo metadata is displayed.',
             extras=[('Use valid sample', 'admin-create-ready'),
                     ('Test duplicate ID', 'admin-create-duplicate')])
    panel('admin-create-discard', 'Discard new profile?',
          ['Nothing has been created yet. No existing student is changed.'],
          [('Keep editing', 'admin-create-ready'), ('Discard profile', 'admin')],
          active='Accounts', role='Administrator')
    panel('admin-create-saved', 'Student profile created',
          ['Mira Demo · DEMO-004 · SE-DEMO',
           'Role: Student · Access restricted to own records',
           'New academic records are empty until assigned results exist.'],
          [('View updated accounts', 'admin-accounts-saved'), ('View new profile', 'admin-created-detail')],
          active='Accounts', role='Administrator')
    panel('admin-created-detail', 'Mira Demo · Profile created',
          ['Institutional ID: DEMO-004 · Group: SE-DEMO',
           'Role: Student · Own records only', 'No grades or achievements yet.'],
          [('Back to accounts', 'admin-accounts-saved')], active='Accounts', role='Administrator')
    for key, ready, error in [('admin-edit', False, None),
                               ('admin-edit-error', False, ['Name cannot be empty. No changes were saved.']),
                               ('admin-edit-ready', True, None)]:
        form(key, 'Edit profile metadata',
             [('Name', 'Dana Sarsen' if key != 'admin-edit-error' else '(empty)', 'admin-edit-ready'),
              ('Institutional ID', 'DEMO-001 · protected identifier', None),
              ('Group', 'SE-DEMO-2' if ready else 'SE-DEMO', 'admin-edit-ready'),
              ('Role', 'Teacher (proposed)' if ready else 'Student', 'admin-role-options')],
             'admin-role-confirm' if ready else 'admin-edit-error', 'admin-edit-discard',
             error=error, note='Review role changes explicitly.\nNew teachers need an assignment.\nGrades cannot be edited here.',
             extras=[('Use revised sample', 'admin-edit-ready'), ('Test empty name', 'admin-edit-error')])
    panel('admin-role-options', 'Select demonstration role',
          ['Student: view own academic records; manage own achievements.',
           'Teacher: view and maintain assigned-course results only.',
           'Administrator: accounts, assignments and grading configuration.',
           'This journey demonstrates changing Dana to Teacher.'],
          [('Choose Teacher', 'admin-edit-ready'), ('Keep Student', 'admin-edit')],
          active='Accounts', role='Administrator')
    panel('admin-edit-discard', 'Discard profile changes?',
          ['The original group and Student role remain unchanged.'],
          [('Keep editing', 'admin-edit-ready'), ('Discard changes', 'admin-account-detail')],
          active='Accounts', role='Administrator')
    panel('admin-role-confirm', 'Confirm profile and role change',
          ['Dana Sarsen · DEMO-001', 'Group: SE-DEMO → SE-DEMO-2 · Role: Student → Teacher',
           'No access to all student records is granted.',
           'An assigned course is required before teaching records are visible.'],
          [('Confirm demo change', 'admin-edit-saved'), ('Back to editing', 'admin-edit-ready')],
          active='Accounts', role='Administrator')
    panel('admin-edit-saved', 'Profile changes saved',
          ['Dana Sarsen · DEMO-001 · SE-DEMO-2',
           'Role: Teacher · No courses assigned yet',
           'Academic results and institutional ID were not changed.'],
          [('View changed profile', 'admin-updated-detail')], active='Accounts', role='Administrator')
    panel('admin-updated-detail', 'Dana Sarsen · Updated profile',
          ['Institutional ID: DEMO-001 · Group: SE-DEMO-2',
           'Role: Teacher · Assigned-course scope only',
           'No assigned courses; no teaching records are visible.',
           'General navigation returns to the baseline demonstration data.'],
          [('Review assignments', 'admin-assignments')], active='Accounts', role='Administrator')

    # Assignment boundaries and duplicate rejection.
    for key, saved in [('admin-assignments', False), ('admin-assignment-list-saved', True)]:
        panel(key, 'Teacher assignments',
              ['Teacher Demo · Software architecture · SE-DEMO · Autumn 2026',
               'Teacher Demo · Database systems · SE-DEMO · Autumn 2026' if saved
               else 'No Database systems assignment exists yet.',
               'An assignment grants access only to its course, group and period.'],
              [('Add assignment', 'admin-assignment-edit'),
               ('Remove assignment', 'admin-assignment-remove') if saved else ('Back to accounts', 'admin')],
              active='Assignments', role='Administrator')
    for key, ready, error in [
        ('admin-assignment-edit', False, None),
        ('admin-assignment-error', False, ['Teacher, course, group and semester are required.']),
        ('admin-assignment-conflict', True, ['This course/group/semester assignment already exists.',
                                           'No duplicate assignment was created.']),
        ('admin-assignment-ready', True, None),
    ]:
        form(key, 'Assign a teacher',
             [('Teacher', 'Teacher Demo' if ready else '(choose teacher)', 'admin-assignment-ready'),
              ('Course', 'Software architecture (duplicate)' if key == 'admin-assignment-conflict'
               else 'Database systems' if ready else '(choose course)', 'admin-assignment-ready'),
              ('Group', 'SE-DEMO' if ready else '(choose group)', 'admin-assignment-ready'),
              ('Semester', 'Autumn 2026' if ready else '(choose semester)', 'admin-assignment-ready')],
             'admin-assignment-confirm' if key == 'admin-assignment-ready' else key if key == 'admin-assignment-conflict' else 'admin-assignment-error',
             'admin-assignment-discard', error=error,
             note='Scope is course + group + term.\nOther students remain inaccessible.\nDuplicate assignments are rejected.',
             extras=[('Use valid assignment', 'admin-assignment-ready'),
                     ('Test duplicate', 'admin-assignment-conflict')])
    panel('admin-assignment-discard', 'Discard assignment changes?',
          ['The existing Software architecture assignment is unchanged.'],
          [('Keep editing', 'admin-assignment-ready'), ('Discard changes', 'admin-assignments')],
          active='Assignments', role='Administrator')
    panel('admin-assignment-confirm', 'Review teacher assignment',
          ['Teacher Demo → Database systems', 'Group: SE-DEMO · Semester: Autumn 2026',
           'Only this assigned course/group/term becomes visible.'],
          [('Confirm assignment', 'admin-assignment-saved'), ('Back to editing', 'admin-assignment-ready')],
          active='Assignments', role='Administrator')
    panel('admin-assignment-saved', 'Teacher assignment saved',
          ['Teacher Demo · Database systems · SE-DEMO · Autumn 2026',
           'The original Software architecture assignment remains active.'],
          [('View updated assignments', 'admin-assignment-list-saved')],
          active='Assignments', role='Administrator')
    panel('admin-assignment-remove', 'Remove demo assignment?',
          ['Teacher Demo · Database systems · SE-DEMO · Autumn 2026',
           'Access through this assignment will end.', 'Existing academic results are preserved.'],
          [('Keep assignment', 'admin-assignment-list-saved'), ('Remove assignment', 'admin-assignment-removed')],
          active='Assignments', role='Administrator')
    panel('admin-assignment-removed', 'Assignment removed',
          ['Database systems access through this assignment is no longer available.',
           'Software architecture remains assigned. Academic results were preserved.'],
          [('View assignments', 'admin-assignments')], active='Assignments', role='Administrator')

    # Versioned grading configuration: draft, validate, preview, confirm, save.
    panel('admin-policy', 'Grading policy · demo-v1',
          ['Illustrative scale: A = 4.00 · B = 3.00 · C = 2.00 · F = 0.00',
           'Credit-weighted GPA · Pending grades excluded · Failed credits included',
           'Round half-up to 2 decimals, only at the final result.',
           'These demo rules are not an approved university policy.'],
          [('Create policy draft', 'admin-grading-edit'), ('Review access scope', 'admin-access')],
          active='Grading policy', role='Administrator')
    panel('admin-access', 'Administrative access boundaries',
          ['Administrators maintain metadata, assignments and grading configuration.',
           'Academic grade changes belong to authorised assigned teachers.',
           'Students cannot change institutional IDs, roles or academic results.',
           'All accounts shown here are fictional.'],
          [('Back to accounts', 'admin')], active='Access scope', role='Administrator')
    for key, ready, error in [('admin-grading-edit', False, None),
                               ('admin-grading-error', False, ['Points must be between 0.00 and 4.00.',
                                                               'Active demo-v1 policy remains unchanged.']),
                               ('admin-grading-ready', True, None)]:
        form(key, 'Draft grading policy · demo-v2',
             [('B grade points', '5.00 (invalid)' if key == 'admin-grading-error' else '3.30' if ready else '3.00', 'admin-grading-ready'),
              ('Other grade points', 'A = 4.00 · C = 2.00 · F = 0.00', None),
              ('GPA and pending grades', 'Credit-weighted · Pending excluded', None),
              ('Rounding / version', 'Half-up · 2 decimals · New version: demo-v2', None)],
             'admin-grading-preview' if ready else 'admin-grading-error', 'admin-grading-discard',
             error=error, note='A draft does not change demo-v1.\nReview calculation impact first.\nNo silent historical recalculation.',
             extras=[('Use valid points 3.30', 'admin-grading-ready'),
                     ('Test invalid points 5.00', 'admin-grading-error')])
    panel('admin-grading-discard', 'Discard policy draft?',
          ['The active policy remains demo-v1.', 'Historical calculations remain linked to their recorded policy.'],
          [('Keep editing', 'admin-grading-ready'), ('Discard draft', 'admin-policy')],
          active='Grading policy', role='Administrator')
    panel('admin-grading-preview', 'Preview grading-policy impact',
          ['Old demo-v1: (5 × 4.00 + 5 × 3.00 + 3 × 4.00) / 13 = 3.62',
           'Draft demo-v2: (5 × 4.00 + 5 × 3.30 + 3 × 4.00) / 13 = 3.73',
           'Preview uses fictional data and final half-up rounding.',
           'Existing records keep demo-v1 unless an explicit migration is agreed.'],
          [('Review activation', 'admin-grading-confirm'), ('Back to editing', 'admin-grading-ready')],
          active='Grading policy', role='Administrator')
    panel('admin-grading-confirm', 'Confirm new grading version',
          ['Activate demo-v2 for the next demonstration calculation.',
           'B changes from 3.00 to 3.30; the 0.00–4.00 range is preserved.',
           'No existing student grades or historical policy versions are overwritten.'],
          [('Activate demo-v2', 'admin-grading-saved'), ('Back to preview', 'admin-grading-preview')],
          active='Grading policy', role='Administrator')
    panel('admin-grading-saved', 'Grading policy saved · demo-v2',
          ['A = 4.00 · B = 3.30 · C = 2.00 · F = 0.00',
           'Credit-weighted · Pending excluded · Final half-up to 2 decimals',
           'Preview fixture: 48.50 / 13 = 3.73.',
           'Historical demo-v1 remains available; no live configuration was changed.'],
          [('View version details', 'admin-grading-version')], active='Grading policy', role='Administrator')
    panel('admin-grading-version', 'Policy versions',
          ['demo-v2 · New demonstration policy · B = 3.30 · Fixture GPA 3.73',
           'demo-v1 · Preserved historical policy · B = 3.00 · Fixture GPA 3.62',
           'General navigation returns to the baseline demo-v1 scenario.'],
          [('Review baseline policy', 'admin-policy'), ('Back to accounts', 'admin')],
          active='Grading policy', role='Administrator')
