import cx_Freeze

executables = [cx_Freeze.Executable('Coach_main.py')]

cx_Freeze.setup(
    name="Coach.py",
    options={'build_exe': {'packages' :['pygame']}},

    executables = executables

)