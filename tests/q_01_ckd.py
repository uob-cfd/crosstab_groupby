test = {
  'name': 'Question ckd',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'ckd'
          >>> 'ckd' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'ckd'
          >>> # from its initial state (of ...)
          >>> ckd is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> isinstance(ckd, pd.DataFrame)
          True
          >>> len(ckd)
          158
          >>> list(ckd)[:5] == ['Age',
          ...                   'Blood Pressure',
          ...                   'Specific Gravity',
          ...                   'Albumin',
          ...                   'Sugar']
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
