test = {
  'name': 'Question pt_dm_medians',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'pt_dm_medians'
          >>> 'pt_dm_medians' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'pt_dm_medians'
          >>> # from its initial state (of ...)
          >>> pt_dm_medians is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> isinstance(pt_dm_medians, pd.DataFrame)
          True
          >>> pt_dm_medians.shape
          (3, 15)
          >>> list(pt_dm_medians)[:5] == ['Age',
          ...                             'Blood Pressure',
          ...                             'Specific Gravity',
          ...                             'Albumin',
          ...                             'Sugar']
          True
          >>> list(pt_dm_medians.T)
          [('CKD', 'no'), ('CKD', 'yes'), ('Not CKD', 'no')]
          >>> np.allclose(np.array(pt_dm_medians)[:, :2],
          ...             [[56. , 80. ],
          ...              [59.5, 80. ],
          ...              [46. , 70. ]])
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
