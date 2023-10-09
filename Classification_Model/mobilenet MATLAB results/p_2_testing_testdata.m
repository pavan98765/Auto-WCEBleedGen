


clc
close all
clear all

load('d_combine_rg_fulldata.mat')
clearvars -except net

%%%%%% ---------- image & pixel datastore -------------------
pth = 'D:\data\BLEEDconf\WCEBleedGen\test\d2 r';
imds = imageDatastore(pth);

tempdir = 'D:\data\BLEEDconf\WCEBleedGen\results_testdata';

pxdsResults = semanticseg(imds,net, ...
    'MiniBatchSize',20, ...
    'WriteLocation',tempdir);
f_str2lab_testdata(pxdsResults,tempdir,'pred');


