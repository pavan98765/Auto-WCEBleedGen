

clc
close all
clear all

dr = f_rem_dir(dir("D:\data\BLEEDconf\WCEBleedGen\results_testdata\pred"));

for i = 1:length(dr)
    im = imread([dr(i).folder '/' dr(i).name]);
    onezero(i,1) = sum(im(:));
end

for i = 1:length(dr)
    if onezero(i,1) == 0
        str(i,1) = "Non-Bleeding";
    else
        str(i,1) = "Bleeding";
    end
end
