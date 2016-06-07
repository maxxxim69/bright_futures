################################################################################
## Script to read the GE's CPS bright futures content from CQIC               ##  
## and convert them into human readable format                                ##
##                                                                            ## 
## John Barnett   2016-06-02                                                  ##
################################################################################


import os

sourceFilesPath = os.curdir + '/eval/'
sourceFiles = os.listdir(sourceFilesPath)
fileCount = 0

"""
Look for "// BEGIN Form Heading: Bright Futures-Initial Newborn Visit"

          1         2         3
0123456789012345678901234567890
// BEGIN Form Heading: Bright Futures-Initial Newborn Visit

BEGIN Form Heading
str1 = "this is string example....wow!!!";
str2 = "exam";

print str1.find(str2)
"""

for source_file in sourceFiles:
	#print(sourceFilesPath + source_file)
	fileCount = fileCount + 1
	LoopCount = 0
	
	open_source_file = open(sourceFilesPath + source_file,'r')
	create_destination_file = open(source_file + '_readable.txt','w')
	
	for line in open_source_file:
		LoopCount = LoopCount + 1
		
		#print(str(LoopCount) + ': ' + line)
		splitLine01 = line.split(',')
		#print(splitLine01)
		
#need to find bf form name
#          1         2         3
#0123456789012345678901234567890
#ccc_Exp_Hx_Exec("F_H","Bright Futures-Initial Newborn Visit","Family Medicine,Pediatrics,Family Practice,Medicine-Pediatrics","Well Child Check||")
		if splitLine01[0] == 'ccc_Exp_Hx_Exec("F_H"':
			formHeader = splitLine01[1]
			lenFormHeader = len(formHeader)
			formHeader = formHeader[1:(lenFormHeader - 1)]
			formHeader = formHeader.strip()
			print('\n\n' + formHeader + '\n')
			create_destination_file.write('\n\n' + formHeader + '\n\n')
		elif splitLine01[0] == 'ccc_Exp_Hx_Exec("D_L"':	
			DropDownName = splitLine01[1]
			DropDownName = DropDownName.strip('"')
			print('\n\n  ' + DropDownName + '\n')  #Column name
			create_destination_file.write('\n\n  ' + DropDownName + '\n\n')
		elif splitLine01[0] == 'ccc_Exp_Hx_Exec("ENDD_L"':   #Ignore this line in the source file
			a = 0 #dummy variable that does nothing
		elif splitLine01[0] == 'ccc_Exp_Hx_Exec("F_HFMT"':   #Ignore this line in the source file
			a = 0 #dummy variable that does nothing
		elif splitLine01[0] == 'ccc_Exp_Hx_Exec("D_LHFMT"':  #Ignore this line in the source file
			a = 0 #dummy variable that does nothing
		elif splitLine01[0] == 'ccc_Exp_Hx_Exec("D_LFMT"':    #Ignore this line in the source file
			a = 0 #dummy variable that does nothing
		elif splitLine01[0] == 'ccc_Exp_Hx_Exec("L_BHFMT"':   #Ignore this line in the source file
			a = 0 #dummy variable that does nothing	
		elif splitLine01[0] == 'ccc_Exp_Hx_Exec("L_BTFMT"':   #Ignore this line in the source file
			a = 0 #dummy variable that does nothing
		elif splitLine01[0] == 'ccc_Exp_Hx_Exec("M_LEF"':     #Ignore this line in the source file
			a = 0 #dummy variable that does nothing
		elif splitLine01[0] == 'ccc_Exp_Hx_Exec("M_LEFOBS"':  #Ignore this line in the source file
			a = 0 #dummy variable that does nothing
		elif splitLine01[0] == 'ccc_Exp_Hx_Exec("M_LEFFMT"':  #Ignore this line in the source file
			a = 0 #dummy variable that does nothing
		elif splitLine01[0] == 'ccc_Exp_Hx_Exec("L_BH1FMT"':  #Ignore this line in the source file
			a = 0 #dummy variable that does nothing
		elif splitLine01[0] == 'ccc_Exp_Hx_Exec("L_BHIND"':   #Ignore this line in the source file
			a = 0 #dummy variable that does nothing
		elif splitLine01[0] == 'ccc_Exp_Hx_Exec("L_B1H"':     #Ignore this line in the source file
			a = 0 #dummy variable that does nothing
		elif splitLine01[0] == 'ccc_Exp_Hx_Exec("GO_TO_TAB"': #Ignore this line in the source file
			a = 0 #dummy variable that does nothing
		elif splitLine01[0] == 'ccc_Exp_Hx_Exec("DEFAULT_LABELS"': #Ignore this line in the source file
			a = 0 #dummy variable that does nothing
		elif splitLine01[0] == 'ccc_Exp_Hx_Exec("L_B"':
			#List Boxes
			listBoxName = splitLine01[1]
			listBoxName = listBoxName.strip('"')
			
			#if the list box is an "empty space, ignore it"
			if len(listBoxName) > 1:
				print('\n\t' + listBoxName + '  [List Box]')
				create_destination_file.write('\n\t' + listBoxName + '  [List Box]\n')
			else:
				a = 0 #dummy variable that does nothing
			
		elif splitLine01[0] == 'ccc_Exp_Hx_Exec("ENDL_B"': #Ignore this line in the source file
			a = 0 #dummy variable that does nothing
		elif splitLine01[0] == 'ccc_Exp_Hx_Exec("EN_D"': #Ignore this line in the source file
			a = 0 #dummy variable that does nothing
		elif splitLine01[0] == 'ccc_Exp_Hx_Exec("A_BUTTON"': #Ignore this line in the source file
			a = 0 #dummy variable that does nothing
		elif splitLine01[0] == 'ccc_Exp_Hx_Exec("LB_MLEF_FMT"': #Ignore this line in the source file
			a = 0 #dummy variable that does nothing
		
		
		else:
			splitLineLen = len(splitLine01)
			if splitLineLen > 1:
				#print(str(splitLineLen))
				
				splitLine01_0 = splitLine01[0]
				splitLine02 = splitLine01_0.split('ccc_Exp_Hx_Exec("')
				splitLine02_1 = splitLine02[1]
				splitLine02_1Len = len(splitLine02_1)
				
				splitLine02_1Final = splitLine02_1[0:splitLine02_1Len-1]
				
				#print(splitLine01_0)
				
				if len(splitLine02_1Final) > 0:
					print('\n\t' + splitLine02_1Final + '  [Dropdown List]')
					create_destination_file.write('\n\t' + splitLine02_1Final + '  [Dropdown List]' + '\n')
					#print(str(len(splitLine02_1Final)))
				
				#grab the dropdown contents
				splitLineDDcontents = line.split('","')
				getDDcontentsBefore2split = splitLineDDcontents[1]
				
				getDDcontentsBefore2split = getDDcontentsBefore2split.strip('^')
				ddContents = getDDcontentsBefore2split.split(',')
				
				if len(ddContents) > 1:
				
					for ddItem in ddContents:
						print('\t\t' + ddItem)
						create_destination_file.write('\t\t' + ddItem + '\n')
				
"""





"""				
				
create_destination_file.close()