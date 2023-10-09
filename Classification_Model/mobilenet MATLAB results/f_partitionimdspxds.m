% % imds = imageDatastore(imgDir);
% % 
% % pxds = pixelLabelDatastore(labelDir,classes,labelIDs);
% % 
% % [imdsTrain, imdsVal, imdsTest, pxdsTrain, pxdsVal, pxdsTest] = partitionCamVidData(imds,pxds);

function [imdsTrain, imdsVal, pxdsTrain, pxdsVal] ...
    = f_partitionimdspxds(imds,pxds,pixelLabelID)


    rng(0); 
    numFiles = numel(imds.Files);
    shuffledIndices = randperm(numFiles);
    
    numTrain = round(0.90 * numFiles);
    trainingIdx = shuffledIndices(1:numTrain);
    
    numVal = round(0.10 * numFiles);
    valIdx = shuffledIndices(numTrain+1:numTrain+numVal);
    
    trainingImages = imds.Files(trainingIdx);
    valImages = imds.Files(valIdx);
    
    imdsTrain = imageDatastore(trainingImages);
    imdsVal = imageDatastore(valImages);
    
    classes = pxds.ClassNames;
    labelIDs = pixelLabelID;
    
    
    trainingLabels = pxds.Files(trainingIdx);
    valLabels = pxds.Files(valIdx);
    
    pxdsTrain = pixelLabelDatastore(trainingLabels, classes, labelIDs);
    pxdsVal = pixelLabelDatastore(valLabels, classes, labelIDs);


% -----------------

end















% % 
% % % % imds = imageDatastore(imgDir);
% % % % 
% % % % pxds = pixelLabelDatastore(labelDir,classes,labelIDs);
% % % % 
% % % % [imdsTrain, imdsVal, imdsTest, pxdsTrain, pxdsVal, pxdsTest] = partitionCamVidData(imds,pxds);
% % 
% % function [imdsTrain, imdsVal, imdsTest, pxdsTrain, pxdsVal, pxdsTest] = f_partitionCamVidData(imds,pxds)
% % % Partition CamVid data by randomly selecting 60% of the data for training. The
% % % rest is used for testing.
% % 
% % % Set initial random state for example reproducibility.
% % rng(0); 
% % numFiles = numel(imds.Files);
% % shuffledIndices = randperm(numFiles);
% % 
% % % Use 80% of the images for training.
% % numTrain = round(0.80 * numFiles);
% % trainingIdx = shuffledIndices(1:numTrain);
% % 
% % % Use 10% of the images for validation
% % numVal = round(0.10 * numFiles);
% % valIdx = shuffledIndices(numTrain+1:numTrain+numVal);
% % 
% % % Use the rest for testing.
% % testIdx = shuffledIndices(numTrain+numVal+1:end);
% % 
% % % Create image datastores for training and test.
% % trainingImages = imds.Files(trainingIdx);
% % valImages = imds.Files(valIdx);
% % testImages = imds.Files(testIdx);
% % 
% % imdsTrain = imageDatastore(trainingImages);
% % imdsVal = imageDatastore(valImages);
% % imdsTest = imageDatastore(testImages);
% % 
% % % Extract class and label IDs info.
% % classes = pxds.ClassNames;
% % labelIDs = camvidPixelLabelIDs();
% % 
% % % Create pixel label datastores for training and test.
% % trainingLabels = pxds.Files(trainingIdx);
% % valLabels = pxds.Files(valIdx);
% % testLabels = pxds.Files(testIdx);
% % 
% % pxdsTrain = pixelLabelDatastore(trainingLabels, classes, labelIDs);
% % pxdsVal = pixelLabelDatastore(valLabels, classes, labelIDs);
% % pxdsTest = pixelLabelDatastore(testLabels, classes, labelIDs);
% % 
% % end