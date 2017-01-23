# Script to generate a Splunk dashboard using only a few inputs
# by Tom Cooling

# $NAME$
# $DESCRIPTION$

import os

start_header = """
<dashboard stylesheet="trafficlight.css">
  <label>$NAME$</label>
  <description>$DESCRIPTION$</description>
"""

end_header = """
</dashboard>"""

start_row = """
  <row>"""

end_row = """
  </row>"""

single_value = """
    <panel>
      <single>
        <title>$NAME$</title>
        <search>
          <query>index="$INDEX$"| stats first($VAR$) as VAR</query>
          <earliest>0</earliest>
          <latest></latest>
          <refresh>$REFRESH$</refresh>
          <refreshType>delay</refreshType>
        </search>
        <option name="colorBy">value</option>
        <option name="colorMode">block</option>
        <option name="height">132</option>
        <option name="rangeColors">["0x65a637","0xd93f3c"]</option>
        <option name="rangeValues">[100000]</option>
        <option name="showSparkline">0</option>
        <option name="showTrendIndicator">0</option>
        <option name="unit">mins</option>
        <option name="useColors">1</option>
      </single>
    </panel>
"""

panels = [["single_value",["$NAME$","Uptime"],["$INDEX$","performance"],["$VAR$","uptime"],["$REFRESH$","30s"]]]

def delete_xml():
    my_file = "dashboard.xml"
    if os.path.isfile(my_file):
        os.remove(my_file)

def generate_dashboard(start_header,start_row,end_row,end_header,panels):
    dashboard = ""

    # Define the strings which will appear in the dashboard
    name = "Test Dashboard"
    description = "This is a test dashboard"

    # Replace strings in the headers with the variables
    start_header = start_header.replace("$NAME$", name)
    start_header = start_header.replace("$DESCRIPTION$", description)

    dashboard += start_header

    # need to add rows here, probably 1 row per 4 graphs/items etc?
    dashboard += start_row

    for p in range(0,len(panels)):
        to_add = eval(panels[p][0])
        for i in range(1,len(panels[p])):
            to_add = to_add.replace(panels[p][i][0],panels[p][i][1])
        dashboard += to_add

    dashboard += end_row

    dashboard += end_header

    # Write to an xml file
    f = open('dashboard.xml', 'w')
    f.write(dashboard)  # python will convert \n to os.linesep
    f.close()

delete_xml()
generate_dashboard(start_header,start_row,end_row,end_header,panels)
