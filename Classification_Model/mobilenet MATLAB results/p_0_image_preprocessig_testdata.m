

%%% --------------------------------------------------------
clc
close all
clear all

pthim = 'D:\data\BLEEDconf\WCEBleedGen\test\d2 ori';
drim = f_rem_dir(dir(pthim));
ch = 1;

if ch == 1
    pthim = 'D:\data\BLEEDconf\WCEBleedGen\test\d2 r';
    parfor i = 1:length(drim)
        disp(num2str(i))
        im = imread([drim(i).folder '/' drim(i).name]);
        im = repmat(im(:,:,1),[1 1 3]);        
        imwrite(im, [pthim '/' drim(i).name]);
    end
end

ch = 2;
if ch == 2
    pthim = 'D:\data\BLEEDconf\WCEBleedGen\test\d2 g';
    parfor i = 1:length(drim)
        disp(num2str(i))
        im = imread([drim(i).folder '/' drim(i).name]);
        im = repmat(im(:,:,2),[1 1 3]);
        imwrite(im, [pthim '/' drim(i).name]);
    end
end


