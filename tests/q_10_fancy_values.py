test = {
  'name': 'Question fancy_values',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'fancy_values'
          >>> 'fancy_values' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'fancy_values'
          >>> # from its initial state (of ...)
          >>> fancy_values is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> isinstance(fancy_values, pd.DataFrame)
          True
          >>> fancy_values.shape
          (2, 2)
          >>> list(fancy_values)
          ['mean_bp', 'median_age']
          >>> list(fancy_values.T)
          ['CKD', 'Not CKD']
          >>> np.allclose(fancy_values, [[80, 59.0], [71.826087, 46.0]])
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
