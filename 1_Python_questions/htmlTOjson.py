import html_to_json
import xmltojson
import json

html_string = """<tr role="row" class="odd"><td><table width="100%"><tbody><tr class="selected"><td><table width="100%"><tbody style="text-align:left;"><tr><td><table id="detail3404095" class="detail-table"><tbody><tr><td valign="TOP"><span style="margin - right:50px; "><a onclick="notify('ViewImage=202309050016140');event.preventDefault();return false;" href="#"><b>Instrument:</b></a> 202309050016140</span><span style="margin - right:50px; "> <b>Volume Page: </b>202309050016140</span><span style="margin - right:50px; "> </span></td></tr><tr><td valign="TOP"><span style="margin - right:50px; "><b>Recorded: </b> 9/5/2023 3:52:14 PM</span><span style="margin - right:50px; "> </span><span style="margin - right:50px; "> <b>Status: </b>Verified</span></td></tr><tr><td valign="TOP"><span style="margin - right:50px; "><b>Document Type: </b> MORTGAGE</span><span style="margin - right:50px; "> <b>Consideration: </b>$8,909.14</span><span style="margin - right:50px; "><b> Pages: </b> 6</span></td></tr><tr><td valign="TOP" colspan="2"><b>Remarks: </b></td></tr><tr><td valign="TOP" colspan="2"><b>Grantor           : </b>STEWART, KAREN L / STEWART, CRAIG A-SR </td></tr><tr><td valign="TOP" colspan="2"><b>Grantee           : </b>SECRETARY OF HOUSING AND URBAN DEV/ SECRETARY OF HOUSING &amp; URBAN DEV</td></tr><tr><td valign="TOP" colspan="2"><b>Legal Description: </b>Sub: SHALIMAR VILLAGE 4TH ADD MADISON TWP Lt: 119<br>
</td></tr><tr><td valign="TOP" colspan="2"><b>Disposition: </b>RFiling - SIMPLIFILE ERECORD SERVICE</td></tr><tr style="display:none"><td><div id="InstrumentReferenceId" style="visibility: hidden">3404095</div></td></tr></tbody></table></td></tr></tbody></table></td></tr></tbody></table></td></tr>"""


# output_json = html_to_json.convert(html_string)
# print(output_json)
# Save the page content as sample.html


html_response = html_string
with open("sample.html", "w") as html_file:
    html_file.write(html_string)

with open("sample.html", "r") as html_file:

    html = '<root>' + html_file.read() + '</root>'
    json_ = xmltojson.parse(html)

with open("data.json", "w") as file:
    json.dump(json_, file)
