voting_data = list(open("voting_record_dump109.txt")) 

voting_dict = create_voting_dict(voting_data)

all_sen_set = { sen_record[0] for sen_record in [ record_str.split() for record_str in voting_data] }
dem_sen_set = { sen_record[0] for sen_record in [ record_str.split() for record_str in voting_data] if sen_record[1] == 'D' }


def create_voting_dict(strlist):
    voting_dic = {}
    for record_entry in strlist:
        record = record_entry.split()
        last_name = record[0]
        party = record[1]
        state = record[2]
        voting_record = [ int(record[i]) for i in range(3, len(record)) ]
        voting_dic[last_name] = voting_record
    return voting_dic
    
def policy_compare(sen_a, sen_b, voting_dict):
    assert sen_a in voting_dict
    assert sen_b in voting_dict
    sen_a_vote_record = voting_dict[sen_a]
    sen_b_vote_record = voting_dict[sen_b]
    dot_product = sum([ a*b for a,b in zip(sen_a_vote_record, sen_b_vote_record) ])
    return dot_product
    
def most_similar(sen, voting_dict):
    assert sen in voting_dict
    sen_vote_record = voting_dict[sen]
    senator_name = ""
    senator_comparison = -1-len(sen_vote_record)
    for k,v in voting_dict.items():
        if k == sen:
            continue
        comparison = policy_compare(sen, k, voting_dict)
        if comparison > senator_comparison:
            senator_name = k
            senator_comparison = comparison
    return (senator_name, senator_comparison)

def least_similar(sen, voting_dict):
    assert sen in voting_dict
    sen_vote_record = voting_dict[sen]
    senator_name = ""
    senator_comparison = 1+len(sen_vote_record)
    for k,v in voting_dict.items():
        if k == sen:
            continue
        comparison = policy_compare(sen, k, voting_dict)
        if comparison < senator_comparison:
            senator_name = k
            senator_comparison = comparison
    return (senator_name, senator_comparison)

def find_average_similarity(sen, sen_set, voting_dict):
    assert sen in voting_dict
    for sen_other in sen_set:
        assert sen_other in voting_dict
        
    n = len(sen_set)
    average_voting_compare = sum([ policy_compare(sen, sen_other, voting_dict) for sen_other in sen_set ])
    return average_voting_compare/n
    
def find_average_record(sen_set, voting_dict):
    sum_votes_per_bill = []
    for sen in sen_set:
        assert sen in voting_dict
        if not sum_votes_per_bill:
            sum_votes_per_bill = voting_dict[sen]
        else:
            sum_votes_per_bill = [ 1 if a == b else -1 if (a + b) == 0 else 0 for a,b in zip(sum_votes_per_bill, voting_dict[sen]) ]
    
    average_record = [ x/len(sen_set) for x in sum_votes_per_bill ]
    return average_record
        
def find_average_record2(sen_set, voting_dict):
    average_record = []
    n = len(sen_set)
    for sen in sen_set:
        assert sen in voting_dict
        if not average_record:
            average_record = [ vote/n for vote in voting_dict[sen] ]
        else:
            average_record = [ a+b for a,b in zip(average_record, [ vote/n for vote in voting_dict[sen] ]) ]
    return average_record
    
def find_most_average_democrat():    
    senator_name = ""
    senator_comparison = -100
    for sen in all_sen_set:
        similarity = find_average_similarity(sen, dem_sen_set, voting_dict)
        if (similarity > senator_comparison):
            if sen == 'Obama' or sen == 'Biden':
                print ("ACCEPT: ({0}, {1})".format(sen, similarity))
            senator_name = sen
            senator_comparison = similarity
        else:
            if sen == 'Obama' or sen == 'Biden':
                print ("REJECT: ({0}, {1})".format(sen, similarity))
            
    return (senator_name, senator_comparison)
        
def find_most_average_democrat2():
    senator_name = ""
    senator_comparison = -100
    
    average_Democrat_record = find_average_record2(dem_sen_set, voting_dict)
    for sen in all_sen_set: 
        sen_vote_record = voting_dict[sen]
        similarity = sum( a*b for a,b in zip(average_Democrat_record, sen_vote_record) )
        if similarity > senator_comparison:
            if sen == 'Obama' or sen == 'Biden':
                print ("ACCEPT: ({0}, {1})".format(sen, similarity))
            senator_name = sen
            senator_comparison = similarity
        else:
            if sen == 'Obama' or sen == 'Biden':
                print ("ACCEPT: ({0}, {1})".format(sen, similarity))
                
    return (senator_name, senator_comparison)    
    
def bitter_rivals():
    senator1_name = ""
    senator2_name = ""
    senator_comparison = 100
    
    for sen1 in all_sen_set:
        for sen2 in all_sen_set:
            if sen1 == sen2:
                continue
            
            similarity = policy_compare(sen1, sen2, voting_dict)
            if similarity < senator_comparison:
                print ("ACCEPT: ({0}, {1}, {2})".format(sen1, sen2, similarity))
                senator1_name = sen1
                senator2_name = sen2
                senator_comparison = similarity
    
    return (senator1_name, senator2_name, senator_comparison)    
    
def bitter_rivals2():
    senator1_name = ""
    senator2_name = ""
    senator_comparison = 100
    
    for sen1 in voting_dict.keys():
        sen2, similarity = least_similar(sen1, voting_dict)
        if similarity < senator_comparison:
            senator_comparison = similarity
            senator1_name = sen1
            senator2_name = sen2
    return (senator1_name, senator2_name, senator_comparison)

            
        
    
    