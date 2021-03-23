test = {
  'name': 'Question ht_pe_by_patient',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'ht_pe_by_patient'
          >>> 'ht_pe_by_patient' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'ht_pe_by_patient'
          >>> # from its initial state (of ...)
          >>> ht_pe_by_patient is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> isinstance(ht_pe_by_patient, pd.DataFrame)
          True
          >>> list(ht_pe_by_patient)
          ['CKD', 'Not CKD']
          >>> list(ht_pe_by_patient.T)
          [('no', 'no'), ('no', 'yes'), ('yes', 'no'), ('yes', 'yes')]
          >>> vals = [[6, 115], [3, 0], [17, 0], [17, 0]]
          >>> np.allclose(np.array(ht_pe_by_patient), vals)
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
