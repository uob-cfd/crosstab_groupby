test = {
  'name': 'Question ht_by_patient',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'ht_by_patient'
          >>> 'ht_by_patient' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'ht_by_patient'
          >>> # from its initial state (of ...)
          >>> ht_by_patient is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> isinstance(ht_by_patient, pd.DataFrame)
          True
          >>> list(ht_by_patient)
          ['CKD', 'Not CKD']
          >>> list(ht_by_patient.T)
          ['no', 'yes']
          >>> np.allclose(np.array(ht_by_patient), [[9, 115], [34, 0]])
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
