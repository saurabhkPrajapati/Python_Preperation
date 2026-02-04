# Initialize a dictionary to map tag keys to indices
tag_mapping = {'Name': 0, 'Project': 1, 'Tier': 2, 'Owner': 3}

# Loop through the tags in reservation['Tags']
for tag in reservation['Tags']:
    key = tag['Key']

    # Check if the tag key is in the mapping
    if key in tag_mapping:
        # Use the mapping to get the index and update the tags list
        tags[tag_mapping[key]] = tag['Value']

# for tag in reservation['Tags']:
#
#     if tag['Key']=='Name' :
#             tags[0] = tag['Value']
#
#     if tag['Key']=='Project' :
#             tags[1] = tag['Value']
#
#     if tag['Key']=='Tier' :
#             tags[2] = tag['Value']
#
#     if tag['Key']=='Owner' :
#             tags[3] = tag['Value']


# _________________________________________________________________________________________________________________________
