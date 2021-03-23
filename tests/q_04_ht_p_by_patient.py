test = {
  'name': 'Question ht_p_by_patient',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'ht_p_by_patient'
          >>> 'ht_p_by_patient' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'ht_p_by_patient'
          >>> # from its initial state (of ...)
          >>> ht_p_by_patient is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> isinstance(ht_p_by_patient, pd.DataFrame)
          True
          >>> list(ht_p_by_patient)
          ['CKD', 'Not CKD']
          >>> list(ht_p_by_patient.T)
          ['no', 'yes']
          >>> vals = np.array([[9, 115], [34, 0]])
          >>> np.allclose(np.array(ht_p_by_patient), vals / vals.sum(axis=0))
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
