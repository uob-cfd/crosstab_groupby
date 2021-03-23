test = {
  'name': 'Question mean_by_patient',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'mean_by_patient'
          >>> 'mean_by_patient' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'mean_by_patient'
          >>> # from its initial state (of ...)
          >>> mean_by_patient is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> isinstance(mean_by_patient, pd.DataFrame)
          True
          >>> mean_by_patient.shape
          (2, 15)
          >>> np.isclose(mean_by_patient.iloc[0, 0], 57.279070)
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
