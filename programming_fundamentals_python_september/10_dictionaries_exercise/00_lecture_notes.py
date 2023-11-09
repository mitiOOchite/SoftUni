some_dict = {
            'mp3':["song1","song2","song3"],
             "mp4":["song2","song3","song4"],
             "video":["song1","song2","song3"]
             }
print(f'\n'.join(some_dict['mp4']))
print(some_dict.keys())
print(some_dict.values())
for key,value in some_dict.items():
    print(f'Key = {key}, value - {value}')
print(sorted(some_dict.values()))
some_dict['mp3'] = some_dict['mp4']
print(some_dict['mp3'])
print(some_dict['mp4'])
pip install simple-salesforce

