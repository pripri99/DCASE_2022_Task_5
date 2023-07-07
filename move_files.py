import os
import shutil

# define source and target directories
source_dir = 'Development_Set/Training_Set/WMW'
target_dir = 'Development_Set/Training_Set/WMW/subfolder'

# create target directory if it does not exist
if not os.path.exists(target_dir):
    os.makedirs(target_dir)

# list all files in source directory
files = ['XC466742.csv', 'XC466157.csv', 'XC208705.csv', 'XC519927.csv', 'XC528227.csv', 'XC145121.csv', 'XC538943.csv', 'XC474019.csv', 'XC478850.csv', 'XC511677.csv', 'XC184429.csv', 'XC511642.csv', 'XC501872.csv', 'XC144531.csv', 'XC180287.csv', 'XC538941.csv', 'XC299330.csv', 'XC422018.csv', 'XC41249.csv', 'XC477331.csv', 'XC487693.csv', 'XC485312.csv', 'XC361804.csv', 'XC341211.csv', 'XC357687.csv', 'XC142515.csv', 'XC476854.csv', 'XC376956.csv', 'XC449187.csv', 'XC479839.csv', 'XC186806.csv', 'XC364458.csv', 'XC100296.csv', 'XC188147.csv', 'XC365601.csv', 'XC343737.csv', 'XC180605.csv', 'XC131532.csv', 'XC483694.csv', 'XC405096.csv', 'XC181349.csv', 'XC314697.csv', 'XC234105.csv', 'XC496443.csv', 'XC236456.csv', 'XC406576.csv', 'XC189883.csv', 'XC538213.csv', 'XC432572.csv', 'XC299495.csv', 'XC483697.csv', 'XC314267.csv', 'XC371002.csv', 'XC473571.csv', 'XC134761.csv', 'XC252756.csv', 'XC100954.csv', 'XC120730.csv', 'XC67350.csv', 'XC296053.csv', 'XC471768.csv', 'XC487692.csv', 'XC475965.csv', 'XC460195.csv', 'XC454603.csv', 'XC324343.csv', 'XC505960.csv', 'XC483906.csv', 'XC185101.csv', 'XC422437.csv', 'XC538710.csv', 'XC428706.csv', 'XC514029.csv', 'XC538467.csv', 'XC120411.csv', 'XC252757.csv', 'XC550870.csv', 'XC299191.csv', 'XC476146.csv', 'XC486755.csv', 'XC440361.csv', 'XC474017.csv', 'XC522864.csv', 'XC149153.csv', 'XC129156.csv', 'XC356856.csv', 'XC90713.csv', 'XC510499.csv', 'XC484626.csv', 'XC417425.csv', 'XC164817.csv', 'XC171122.csv', 'XC420542.csv', 'XC522273.csv', 'XC196976.csv', 'XC511674.csv', 'XC253273.csv', 'XC141571.csv', 'XC31615.csv', 'XC106971.csv', 'XC448652.csv', 'XC422019.csv', 'XC185104.csv', 'XC171445.csv', 'XC134051.csv', 'XC326162.csv', 'XC270427.csv', 'XC150591.csv', 'XC100619.csv', 'XC448653.csv', 'XC379953.csv', 'XC135278.csv', 'XC495092.csv', 'XC510571.csv', 'XC417089.csv', 'XC143954.csv', 'XC280997.csv', 'XC281357.csv', 'XC357911.csv', 'XC315733.csv', 'XC336861.csv', 'XC141170.csv', 'XC100622.csv', 'XC519898.csv', 'XC26959.csv', 'XC526238.csv', 'XC440482.csv', 'XC240134.csv', 'XC379838.csv', 'XC317421.csv', 'XC42542.csv', 'XC134762.csv', 'XC263296.csv', 'XC416949.csv', 'XC318427.csv', 'XC511641.csv', 'XC447442.csv', 'XC538478.csv', 'XC312051.csv', 'XC457036.csv', 'XC146712.csv', 'XC544680.csv', 'XC135658.csv', 'XC379837.csv', 'XC477007.csv', 'XC488409.csv', 'XC189882.csv', 'XC30134.csv', 'XC42541.csv', 'XC459669.csv', 'XC467851.csv', 'XC479978.csv', 'XC134219.csv', 'XC469959.csv', 'XC432145.csv', 'XC515865.csv', 'XC416749.csv', 'XC245725.csv', 'XC281359.csv', 'XC109629.csv', 'XC103243.csv', 'XC376956.wav', 'XC357911.wav', 'XC263296_mel_un_normalized.npy', 'XC336861_mel_un_normalized.npy', 'XC357911_mel_un_normalized.npy', 'XC379837_mel_un_normalized.npy', 'XC376956_mel_un_normalized.npy', 'XC460195_mel_un_normalized.npy', 'XC466157_mel_un_normalized.npy', 'XC457036_mel_un_normalized.npy', 'XC477331_mel_un_normalized.npy', 'XC485312_mel_un_normalized.npy', 'XC501872_mel_un_normalized.npy', 'XC510499_mel_un_normalized.npy', 'XC510571_mel_un_normalized.npy', 'XC515865_mel_un_normalized.npy', 'XC522273_mel_un_normalized.npy', 'XC526238_mel_un_normalized.npy', 'XC263296_mel.npy', 'XC336861_mel.npy', 'XC379837_mel.npy', 'XC357911_mel.npy', 'XC376956_mel.npy', 'XC457036_mel.npy', 'XC460195_mel.npy', 'XC466157_mel.npy', 'XC477331_mel.npy', 'XC485312_mel.npy', 'XC501872_mel.npy', 'XC510571_mel.npy', 'XC510499_mel.npy', 'XC522273_mel.npy', 'XC515865_mel.npy', 'XC526238_mel.npy', 'XC263296_logmel.npy', 'XC336861_logmel.npy', 'XC376956_logmel.npy', 'XC379837_logmel.npy', 'XC357911_logmel.npy', 'XC466157_logmel.npy', 'XC457036_logmel.npy', 'XC460195_logmel.npy', 'XC477331_logmel.npy', 'XC501872_logmel.npy', 'XC526238_logmel.npy', 'XC522273_logmel.npy', 'XC485312_logmel.npy', 'XC515865_logmel.npy', 'XC510499_logmel.npy', 'XC510571_logmel.npy', 'XC263296_pcen.npy', 'XC336861_pcen.npy', 'XC357911_pcen.npy', 'XC376956_pcen.npy', 'XC379837_pcen.npy', 'XC466157_pcen.npy', 'XC460195_pcen.npy', 'XC457036_pcen.npy', 'XC510499_pcen.npy', 'XC485312_pcen.npy', 'XC477331_pcen.npy', 'XC510571_pcen.npy', 'XC501872_pcen.npy', 'XC526238_pcen.npy', 'XC515865_pcen.npy', 'XC522273_pcen.npy', 'XC188147_mfcc.npy', 'XC142515_mfcc.npy', 'XC131532_mfcc.npy', 'XC144531_mfcc.npy', 'XC185101_mfcc.npy', 'XC149153_mfcc.npy', 'XC134761_mfcc.npy', 'XC189882_mfcc.npy', 'XC134762_mfcc.npy', 'XC120411_mfcc.npy', 'XC100296_mfcc.npy', 'XC145121_mfcc.npy', 'XC100954_mfcc.npy', 'XC164817_mfcc.npy', 'XC135658_mfcc.npy', 'XC180287_mfcc.npy', 'XC150591_mfcc.npy', 'XC189883_mfcc.npy', 'XC120730_mfcc.npy', 'XC106971_mfcc.npy', 'XC186806_mfcc.npy', 'XC134219_mfcc.npy', 'XC180605_mfcc.npy', 'XC100619_mfcc.npy', 'XC134051_mfcc.npy', 'XC143954_mfcc.npy', 'XC129156_mfcc.npy', 'XC181349_mfcc.npy', 'XC141571_mfcc.npy', 'XC185104_mfcc.npy', 'XC141170_mfcc.npy', 'XC422437_mfcc.npy', 'XC379953_mfcc.npy', 'XC476146_mfcc.npy', 'XC484626_mfcc.npy', 'XC454603_mfcc.npy', 'XC476854_mfcc.npy', 'XC326162_mfcc.npy', 'XC417089_mfcc.npy', 'XC475965_mfcc.npy', 'XC449187_mfcc.npy', 'XC473571_mfcc.npy', 'XC236456_mfcc.npy', 'XC483906_mfcc.npy', 'XC208705_mfcc.npy', 'XC365601_mfcc.npy', 'XC343737_mfcc.npy', 'XC428706_mfcc.npy', 'XC234105_mfcc.npy', 'XC314697_mfcc.npy', 'XC479978_mfcc.npy', 'XC196976_mfcc.npy', 'XC416949_mfcc.npy', 'XC486755_mfcc.npy', 'XC299191_mfcc.npy', 'XC460195_mfcc.npy', 'XC324343_mfcc.npy', 'XC457036_mfcc.npy', 'XC448653_mfcc.npy', 'XC422018_mfcc.npy', 'XC42541_mfcc.npy', 'XC41249_mfcc.npy', 'XC466742_mfcc.npy', 'XC336861_mfcc.npy', 'XC280997_mfcc.npy', 'XC30134_mfcc.npy', 'XC361804_mfcc.npy', 'XC469959_mfcc.npy', 'XC281359_mfcc.npy', 'XC341211_mfcc.npy', 'XC440482_mfcc.npy', 'XC405096_mfcc.npy', 'XC314267_mfcc.npy', 'XC356856_mfcc.npy', 'XC376956_mfcc.npy', 'XC467851_mfcc.npy', 'XC371002_mfcc.npy', 'XC448652_mfcc.npy', 'XC299495_mfcc.npy', 'XC296053_mfcc.npy', 'XC487693_mfcc.npy', 'XC485312_mfcc.npy', 'XC315733_mfcc.npy', 'XC483694_mfcc.npy', 'XC31615_mfcc.npy', 'XC379838_mfcc.npy', 'XC252757_mfcc.npy', 'XC459669_mfcc.npy', 'XC281357_mfcc.npy', 'XC495092_mfcc.npy', 'XC263296_mfcc.npy', 'XC252756_mfcc.npy', 'XC312051_mfcc.npy', 'XC483697_mfcc.npy', 'XC432145_mfcc.npy', 'XC474017_mfcc.npy', 'XC432572_mfcc.npy', 'XC270427_mfcc.npy', 'XC474019_mfcc.npy', 'XC496443_mfcc.npy', 'XC466157_mfcc.npy', 'XC487692_mfcc.npy', 'XC26959_mfcc.npy', 'XC364458_mfcc.npy', 'XC357911_mfcc.npy', 'XC447442_mfcc.npy', 'XC245725_mfcc.npy', 'XC379837_mfcc.npy', 'XC477331_mfcc.npy', 'XC477007_mfcc.npy', 'XC240134_mfcc.npy', 'XC417425_mfcc.npy', 'XC42542_mfcc.npy', 'XC479839_mfcc.npy', 'XC526238_mfcc.npy', 'XC538467_mfcc.npy', 'XC510571_mfcc.npy', 'XC511674_mfcc.npy', 'XC501872_mfcc.npy', 'XC514029_mfcc.npy', 'XC519898_mfcc.npy', 'XC90713_mfcc.npy', 'XC511642_mfcc.npy', 'XC505960_mfcc.npy', 'XC538478_mfcc.npy', 'XC538943_mfcc.npy', 'XC67350_mfcc.npy', 'XC510499_mfcc.npy', 'XC538941_mfcc.npy', 'XC515865_mfcc.npy', 'XC522273_mfcc.npy', 'XC538213_mfcc.npy', 'XC528227_mfcc.npy', 'XC538710_mfcc.npy', 'XC550870_mfcc.npy', 'XC544680_mfcc.npy', 'XC141170_delta_mfcc.npy', 'XC106971_delta_mfcc.npy', 'XC100619_delta_mfcc.npy', 'XC131532_delta_mfcc.npy', 'XC134219_delta_mfcc.npy', 'XC100296_delta_mfcc.npy', 'XC135658_delta_mfcc.npy', 'XC100954_delta_mfcc.npy', 'XC120411_delta_mfcc.npy', 'XC134762_delta_mfcc.npy', 'XC120730_delta_mfcc.npy', 'XC134051_delta_mfcc.npy', 'XC129156_delta_mfcc.npy', 'XC134761_delta_mfcc.npy', 'XC188147_delta_mfcc.npy', 'XC447442_delta_mfcc.npy', 'XC326162_delta_mfcc.npy', 'XC376956_delta_mfcc.npy', 'XC432572_delta_mfcc.npy', 'XC42541_delta_mfcc.npy', 'XC379953_delta_mfcc.npy', 'XC459669_delta_mfcc.npy', 'XC144531_delta_mfcc.npy', 'XC457036_delta_mfcc.npy', 'XC189883_delta_mfcc.npy', 'XC312051_delta_mfcc.npy', 'XC196976_delta_mfcc.npy', 'XC186806_delta_mfcc.npy', 'XC416949_delta_mfcc.npy', 'XC281359_delta_mfcc.npy', 'XC141571_delta_mfcc.npy', 'XC422018_delta_mfcc.npy', 'XC234105_delta_mfcc.npy', 'XC299191_delta_mfcc.npy', 'XC364458_delta_mfcc.npy', 'XC180287_delta_mfcc.npy', 'XC405096_delta_mfcc.npy', 'XC343737_delta_mfcc.npy', 'XC448653_delta_mfcc.npy', 'XC448652_delta_mfcc.npy', 'XC314697_delta_mfcc.npy', 'XC149153_delta_mfcc.npy', 'XC449187_delta_mfcc.npy', 'XC299495_delta_mfcc.npy', 'XC185101_delta_mfcc.npy', 'XC460195_delta_mfcc.npy', 'XC42542_delta_mfcc.npy', 'XC181349_delta_mfcc.npy', 'XC30134_delta_mfcc.npy', 'XC466742_delta_mfcc.npy', 'XC365601_delta_mfcc.npy', 'XC281357_delta_mfcc.npy', 'XC324343_delta_mfcc.npy', 'XC252756_delta_mfcc.npy', 'XC236456_delta_mfcc.npy', 'XC417425_delta_mfcc.npy', 'XC280997_delta_mfcc.npy', 'XC466157_delta_mfcc.npy', 'XC422437_delta_mfcc.npy', 'XC150591_delta_mfcc.npy', 'XC41249_delta_mfcc.npy', 'XC180605_delta_mfcc.npy', 'XC417089_delta_mfcc.npy', 'XC208705_delta_mfcc.npy', 'XC142515_delta_mfcc.npy', 'XC31615_delta_mfcc.npy', 'XC473571_delta_mfcc.npy', 'XC296053_delta_mfcc.npy', 'XC189882_delta_mfcc.npy', 'XC440482_delta_mfcc.npy', 'XC143954_delta_mfcc.npy', 'XC270427_delta_mfcc.npy', 'XC164817_delta_mfcc.npy', 'XC379837_delta_mfcc.npy', 'XC356856_delta_mfcc.npy', 'XC474017_delta_mfcc.npy', 'XC245725_delta_mfcc.npy', 'XC26959_delta_mfcc.npy', 'XC185104_delta_mfcc.npy', 'XC315733_delta_mfcc.npy', 'XC314267_delta_mfcc.npy', 'XC361804_delta_mfcc.npy', 'XC469959_delta_mfcc.npy', 'XC371002_delta_mfcc.npy', 'XC379838_delta_mfcc.npy', 'XC467851_delta_mfcc.npy', 'XC263296_delta_mfcc.npy', 'XC428706_delta_mfcc.npy', 'XC145121_delta_mfcc.npy', 'XC252757_delta_mfcc.npy', 'XC454603_delta_mfcc.npy', 'XC341211_delta_mfcc.npy', 'XC240134_delta_mfcc.npy', 'XC432145_delta_mfcc.npy', 'XC336861_delta_mfcc.npy', 'XC357911_delta_mfcc.npy', 'XC483697_delta_mfcc.npy', 'XC505960_delta_mfcc.npy', 'XC476854_delta_mfcc.npy', 'XC538943_delta_mfcc.npy', 'XC483906_delta_mfcc.npy', 'XC538467_delta_mfcc.npy', 'XC538213_delta_mfcc.npy', 'XC510571_delta_mfcc.npy', 'XC511674_delta_mfcc.npy', 'XC550870_delta_mfcc.npy', 'XC528227_delta_mfcc.npy', 'XC479978_delta_mfcc.npy', 'XC486755_delta_mfcc.npy', 'XC514029_delta_mfcc.npy', 'XC487693_delta_mfcc.npy', 'XC511642_delta_mfcc.npy', 'XC477331_delta_mfcc.npy', 'XC475965_delta_mfcc.npy', 'XC496443_delta_mfcc.npy', 'XC538941_delta_mfcc.npy', 'XC522273_delta_mfcc.npy', 'XC479839_delta_mfcc.npy', 'XC487692_delta_mfcc.npy', 'XC515865_delta_mfcc.npy', 'XC519898_delta_mfcc.npy', 'XC67350_delta_mfcc.npy', 'XC90713_delta_mfcc.npy', 'XC495092_delta_mfcc.npy', 'XC485312_delta_mfcc.npy', 'XC484626_delta_mfcc.npy', 'XC510499_delta_mfcc.npy', 'XC501872_delta_mfcc.npy', 'XC477007_delta_mfcc.npy', 'XC538710_delta_mfcc.npy', 'XC474019_delta_mfcc.npy', 'XC526238_delta_mfcc.npy', 'XC544680_delta_mfcc.npy', 'XC538478_delta_mfcc.npy', 'XC483694_delta_mfcc.npy', 'XC476146_delta_mfcc.npy', 'XC26959_spec.npy', 'XC31615.wav', 'XC30134_spec.npy', 'XC30134_pcen.npy', 'XC30134_mel_un_normalized.npy', 'XC30134_mel.npy', 'XC30134_logmel.npy', 'XC30134.wav', 'XC41249_logmel.npy', 'XC41249.wav', 'XC31615_spec.npy', 'XC31615_pcen.npy', 'XC31615_mel_un_normalized.npy', 'XC31615_mel.npy', 'XC31615_logmel.npy', 'XC42542_spec.npy', 'XC42542_pcen.npy', 'XC42542_mel_un_normalized.npy', 'XC42542_mel.npy', 'XC42542_logmel.npy', 'XC42542.wav', 'XC42541_spec.npy', 'XC42541_pcen.npy', 'XC42541_mel_un_normalized.npy', 'XC42541_mel.npy', 'XC42541_logmel.npy', 'XC42541.wav', 'XC41249_spec.npy', 'XC41249_pcen.npy', 'XC41249_mel_un_normalized.npy', 'XC41249_mel.npy', 'XC90713.wav', 'XC67350_spec.npy', 'XC67350_pcen.npy', 'XC67350_mel_un_normalized.npy', 'XC67350_mel.npy', 'XC67350_logmel.npy', 'XC67350.wav', 'XC100296_mel_un_normalized.npy', 'XC100296_mel.npy', 'XC100296_logmel.npy', 'XC100296.wav', 'XC90713_spec.npy', 'XC90713_pcen.npy', 'XC90713_mel_un_normalized.npy', 'XC90713_mel.npy', 'XC90713_logmel.npy', 'XC100619_pcen.npy', 'XC100619_mel_un_normalized.npy', 'XC100619_mel.npy', 'XC100619_logmel.npy', 'XC100619.wav', 'XC100296_spec.npy', 'XC100296_pcen.npy', 'XC100622_mfcc.npy', 'XC100622_mel_un_normalized.npy', 'XC100622_mel.npy', 'XC100622_logmel.npy', 'XC100622_delta_mfcc.npy', 'XC100622.wav', 'XC100619_spec.npy', 'XC100954_spec.npy', 'XC100954_pcen.npy', 'XC100954_mel_un_normalized.npy', 'XC100954_mel.npy', 'XC100954_logmel.npy', 'XC100954.wav', 'XC100622_spec.npy', 'XC100622_pcen.npy', 'XC103243_mfcc.npy', 'XC103243_mel_un_normalized.npy', 'XC103243_mel.npy', 'XC103243_logmel.npy', 'XC103243_delta_mfcc.npy', 'XC103243.wav', 'XC106971_mel.npy', 'XC106971_logmel.npy', 'XC106971.wav', 'XC103243_spec.npy', 'XC103243_pcen.npy', 'XC109629_logmel.npy', 'XC109629_delta_mfcc.npy', 'XC109629.wav', 'XC106971_spec.npy', 'XC106971_pcen.npy', 'XC106971_mel_un_normalized.npy', 'XC109629_spec.npy', 'XC109629_pcen.npy', 'XC109629_mfcc.npy', 'XC109629_mel_un_normalized.npy', 'XC109629_mel.npy', 'XC120411_spec.npy', 'XC120411_pcen.npy', 'XC120411_mel_un_normalized.npy', 'XC120411_mel.npy', 'XC120411_logmel.npy', 'XC120411.wav', 'XC120730_spec.npy', 'XC120730_pcen.npy', 'XC120730_mel_un_normalized.npy', 'XC120730_mel.npy', 'XC120730_logmel.npy', 'XC120730.wav', 'XC129156_pcen.npy', 'XC129156_mel_un_normalized.npy', 'XC129156_mel.npy', 'XC129156_logmel.npy', 'XC129156.wav', 'XC131532_spec.npy', 'XC131532_pcen.npy', 'XC131532_mel_un_normalized.npy', 'XC131532_mel.npy', 'XC131532_logmel.npy', 'XC131532.wav', 'XC129156_spec.npy', 'XC134051_spec.npy', 'XC134051_pcen.npy', 'XC134051_mel_un_normalized.npy', 'XC134051_mel.npy', 'XC134051_logmel.npy', 'XC134051.wav', 'XC134219_spec.npy', 'XC134219_pcen.npy', 'XC134219_mel_un_normalized.npy', 'XC134219_mel.npy', 'XC134219_logmel.npy', 'XC134219.wav', 'XC134761_spec.npy', 'XC134761_pcen.npy', 'XC134761_mel_un_normalized.npy', 'XC134761_mel.npy', 'XC134761_logmel.npy', 'XC134761.wav', 'XC134762_spec.npy', 'XC134762_pcen.npy', 'XC134762_mel_un_normalized.npy', 'XC134762_mel.npy', 'XC134762_logmel.npy', 'XC134762.wav', 'XC135278_delta_mfcc.npy', 'XC135278.wav', 'XC135278_mfcc.npy', 'XC135278_mel_un_normalized.npy', 'XC135278_mel.npy', 'XC135278_logmel.npy', 'XC135278_spec.npy', 'XC135278_pcen.npy', 'XC26959_pcen.npy', 'XC26959_mel_un_normalized.npy', 'XC26959_mel.npy', 'XC26959_logmel.npy', 'XC135658_mel_un_normalized.npy', 'XC135658_mel.npy', 'XC135658_logmel.npy', 'XC135658.wav', 'XC26959.wav']
# move all files to target directory
for file in files:
    try:
        shutil.move(os.path.join(source_dir, file), target_dir)
    except:
        pass


print(f"Moved {len(files)} files.")
