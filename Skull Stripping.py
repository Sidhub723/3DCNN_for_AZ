# import os
# import nipype
# import nipype.interfaces.fsl as fsl

# data_dir='C:/Users/Siddharth/Downloads/ADNI1_Complete 1Yr 1.5T_small/ADNI/141_S_1152/MPR__GradWarp__B1_Correction__N3__Scaled/2006-12-26_15_23_11.0\I48590/'                                             #image directory
# ssdata_dir='ADNI_141_S_1152_MR_MPR__GradWarp__B1_Correction__N3__Scaled_Br_20070411123107490_S24487_I48590.nii'                                                                                                                            #path to skull stripped image directory

# for file in os.listdir(data_dir):
#     try:
#         # mybet = nipype.interfaces.fsl.BET(in_file=os.path.join(data_dir,file),out_file=os.path.join(ssdata_dir,file +'_2.nii'), fac=0.2)                #frac=0.2
#         mybet = nipype.interfaces.fsl.BET(in_file=data_dir+ssdata_dir, out_file=data_dir+ssdata_dir+'_2.nii', frac=0.2)                #frac=0.2

#         res = mybet.run()                                                                                                                                      #executing the brain extraction
#         print(file+'is skull stripped')
#     except:
#         print(file+'is not skull stripped')


import nipype.interfaces.fsl as fsl

bet = fsl.BET()

input_file = 'C:/Users/Siddharth/Downloads/ADNI1_Complete 1Yr 1.5T_small/ADNI/141_S_1152/MPR__GradWarp__B1_Correction__N3__Scaled/2006-12-26_15_23_11.0\I48590/ADNI_141_S_1152_MR_MPR__GradWarp__B1_Correction__N3__Scaled_Br_20070411123107490_S24487_I48590.nii'

bet.inputs.in_file = input_file
bet.inputs.out_file = 'C:/Users/Siddharth/Downloads/ADNI1_Complete 1Yr 1.5T_small/ADNI/141_S_1152/MPR__GradWarp__B1_Correction__N3__Scaled/2006-12-26_15_23_11.0\I48590/OUTPUT.nii'

bet.inputs.frac = 0.3  # Adjust based on your needs

result = bet.run()

print(f"Skull-stripped image saved at: {bet.inputs.out_file}")

    
