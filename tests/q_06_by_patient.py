test = {
  'name': 'Question by_patient',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'by_patient'
          >>> 'by_patient' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'by_patient'
          >>> # from its initial state (of ...)
          >>> by_patient is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # It this a GroupBy object?
          >>> hasattr(by_patient, 'get_group')
          True
          >>> len(by_patient)
          2
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
