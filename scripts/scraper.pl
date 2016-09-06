#!/bin/perl

# we scrape FE3 stats for all FE1/3/11/12 characters
# because serenes' layout for SD/NM sucks donkeys
@games = ("mystery-of-the-emblem/characters", "genealogy-of-the-holy-war/characters", "thracia-776/characters", "binding-blade/characters", "blazing-sword/characters", "the-sacred-stones/characters", "path-of-radiance/characters", "radiant-dawn/characters", "awakening/characters", "fire-emblem-fates/nohrian-characters", "fire-emblem-fates/hoshidan-characters");

open($f, '>', 'bases.csv') or die "failed to open file";

foreach $game (@games) {
    $page = `wget -q -O- "http://serenesforest.net/$game/base-stats/" | egrep "<td>|<tr>" | tr '\n' ','`;
    $page =~ s/<\/?td>//g;
    $page =~ s/,?<tr>,?/\n/g;
    print $f $page;
}

close $f;
open($f, '>', 'growths.csv') or die "failed to open file";

foreach $game (@games) {
    $page = `wget -q -O- "http://serenesforest.net/$game/growth-rates/" | egrep "<td>|<tr>" | tr '\n' ','`;
    $page =~ s/<\/?td>//g;
    $page =~ s/,?<tr>,?/\n/g;
    print $f $page;
}

close $f;
open($f, '>', 'items.csv') or die "failed to open file";

foreach $game (@games) {
    # thanks serenes
    if ($game =~ "ra.ia|fates") {
                # btw i love this regex
                # it hits "radiant", "radiance" and "thRAcIA" all at once.
        $page = `wget -q -O- "http://serenesforest.net/$game/other-data/" | egrep "<td>|<tr>" | tr '\n' ','`;
    } else {
        $page = `wget -q -O- "http://serenesforest.net/$game/starting-items/" | egrep "<td>|<tr>" | tr '\n' ','`;
    }   
    $page =~ s/<\/?td>//g;
    $page =~ s/,?<tr>,?/\n/g;
    print $f $page;
}

close $f;

# the formatting isn't perfect after this
# notably, some games have STR/MAG split and others don't
# have to remove all the MAG stats and just merge them into "POW"
# also have to remove all the icons, weapon ranks, skills and stuff
# plus combine everything into one file with all the numbers aligned properly
# but i'll do that manually because too many shitty edge cases