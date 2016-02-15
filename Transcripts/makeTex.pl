#!/usr/bin/perl

#Just a small script to reformat the Udacity/Google Deep learning course transcripts 
#into something a little easier to read

#gets list of directories
$cwd='.';
opendir $dh, $cwd;
my @dirs = grep {-d "$cwd/$_" && ! /^\.{1,2}$/} readdir($dh);

$header='\documentclass{article}
\usepackage{fullpage}
\begin{document}'."\n";

foreach $dirName (@dirs)
{
    $texFileName=$dirName; #texFile shares name with directory
    $texFileName=~s/\s*Subtitles\s*//; 
    $texFileName=~s/ /-/g; #replace spaces with dashes
    $texFileName= "$texFileName".'.tex';
    open TEXFILE, ">", $texFileName; 
    print TEXFILE "$header";
    chomp(@files=`ls "$dirName"|grep ".srt"`);
    foreach $srtFile (@files)
    {
        $text=`grep [a-z] '$dirName/$srtFile'`; #include all lines with words
        $srtFile=~s/^.*?([A-Z])/$1/;
        $srtFile=~s/\.srt//;
        print TEXFILE "\\section{$srtFile}\n"; #section headers same as file names
        print TEXFILE $text;
    }
    print TEXFILE "\n".'\end{document}';
    system("pdflatex $texFileName");
}

