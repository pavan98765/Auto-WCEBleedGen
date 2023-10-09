

clc
close all
clear all

%%%%%% ---------- image & pixel datastore -------------------
pth = 'D:\data\BLEEDconf\WCEBleedGen\combine\r';
imds = imageDatastore(pth);
pth = 'D:\data\BLEEDconf\WCEBleedGen\combine\Annotations';
classNames = ["zero" "one"];
pixelLabelID = [0 1];
pxds = pixelLabelDatastore(pth,classNames,pixelLabelID);

pth = 'D:\data\BLEEDconf\WCEBleedGen\combine\g';
imds1 = imageDatastore(pth);
pth = 'D:\data\BLEEDconf\WCEBleedGen\combine\Annotations';
pxds1 = pixelLabelDatastore(pth,classNames,pixelLabelID);

imds = imageDatastore([imds.Files; imds1.Files]);
pxds = pixelLabelDatastore([pxds.Files; pxds1.Files],classNames,pixelLabelID);

ds = combine(imds,pxds);

clear imds1 pxds1
tbl = countEachLabel(pxds);
imageFreq = tbl.PixelCount ./ tbl.ImagePixelCount;
classWeights = median(imageFreq) ./ imageFreq;

%%%%%% -----------------------------------

imageSize = [224 224 3];
numClasses = length(classNames);

lgraph = deeplabv3plusLayers(imageSize, numClasses, "mobilenetv2");
pxLayer = pixelClassificationLayer('Name','labels','Classes',tbl.Name,'ClassWeights',classWeights);
lgraph = replaceLayer(lgraph,"classification",pxLayer);

% Define training options. 
options = trainingOptions('sgdm', ...
    'LearnRateSchedule','piecewise',...
    'LearnRateDropPeriod',10,...
    'LearnRateDropFactor',0.3,...
    'InitialLearnRate',1e-3, ...
    'MaxEpochs',30, ...  
    'MiniBatchSize',40, ...
    'Shuffle','every-epoch'); %, ...     'Plots','training-progress');

[net, info] = trainNetwork(ds,lgraph,options);
save('d_combine_rg_fulldata','net')

