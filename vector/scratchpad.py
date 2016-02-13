import plotting
import voting_record

sen_voting_data = list(open("voting_record_dump109.txt")) 

dem_sen_voting_data = [ (sen_vote_record[0], sen_vote_record[3:]) for sen_vote_record in [ sen_vote_record_string.split() for sen_vote_record_string in sen_voting_data] if sen_vote_record[1] == 'D']

all_sen_set = { sen_vote_record[0] for sen_vote_record in [ sen_vote_record_string.split() for sen_vote_record_string in sen_voting_data] }
dem_sen_set = { sen_vote_record[0] for sen_vote_record in [ sen_vote_record_string.split() for sen_vote_record_string in sen_voting_data] if sen_vote_record[1] == 'D' }

average_Democrat_record = voting_record.find_average_record2(dem_sen_set, voting_record.voting_dict)


