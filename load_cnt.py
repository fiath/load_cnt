"""load_cnt - module for loading NeuroScan continuous file
Usage:
  >> cnt = loadcnt(file, varargin)

 Inputs:
   filename - name of the file with extension

 Optional inputs:
  't1'         - start at time t1, default 0
  'sample1'    - start at sample1, default 0, overrides t1
  'lddur'      - duration of segment to load, default = whole file
  'ldnsamples' - number of samples to load, default = whole file,
                 overrides lddur
  'scale'      - ['on'|'off'] scale data to microvolt (default:'on')
  'dataformat' - ['int16'|'int32'] default is 'int16' for 16-bit data.
                 Use 'int32' for 32-bit data.
  'blockread'  - [integer] by default it is automatically determined
                 from the file header, though sometimes it finds an
                 incorect value, so you may want to enter a value manually
                 here (1 is the most standard value).

Outputs:
  cnt          - structure with the continuous data and other informations
              cnt.header
              cnt.electloc
               cnt.data
              cnt.tag
"""






