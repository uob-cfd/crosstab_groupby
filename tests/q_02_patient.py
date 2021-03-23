test = {
  'name': 'Question 02_patient',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to make a "Patient" column.
          >>> 'Patient' in ckd
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.all(ckd.loc[ckd['Class'] == 1, 'Patient'] == 'CKD')
          True
          >>> np.all(ckd.loc[ckd['Class'] == 0, 'Patient'] == 'Not CKD')
          True
          """,
          'hidden': False,
          'locked': False
        },
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
