f = open("NH-A_10_dense.bed", "r")
ans = open("NH-A_10_dense_mod.bed", "w")
start_bed = True
for line in f:
    if start_bed == True:
        start_bed = False
        ans.write(line)
        pass
    else:
        current_str = list(line.strip().split('\t'))
        if current_str[3] == '1':
            tp = 'Weak_promoter'
        elif current_str[3] == '2':
            tp = 'Repressed_heterochromatin'
        elif current_str[3] == '3':
            tp = 'Transcriptional_transition'
        elif current_str[3] == '4':
            tp = 'Transcriptional_elonation'
        elif current_str[3] == '5':
            tp = 'Polycomb_repressed'
        elif current_str[3] == '6':
            tp = 'Intron'
        elif current_str[3] == '7':
            tp = 'Strong_enhancer'
        elif current_str[3] == '8':
            tp = 'Weak_enhancer'
        elif current_str[3] == '9':
            tp = 'Insulator'
        elif current_str[3] == '10':
            tp = 'Active_promoter'
        ans.write(current_str[0] + '\t' + current_str[1] + '\t' + current_str[2] + '\t' + tp + '\t' + current_str[4] +
                  '\t' + current_str[5] + '\t' + current_str[6] + '\t' + current_str[7] + '\t' + current_str[8] + '\t' + '\n')
f.close()
ans.close()
