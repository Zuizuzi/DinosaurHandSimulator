#All the combos assume that Scrap Chimera is present in the deck. Drawing it does not change anything in any combo. Linkuriboh in Extra is needed somewhere IIRC, alos wyvern of course

def IsHandFullCombo(Hand,DeckRem):
    """Determines whether a hand can manke 3 Rank 4 XYZ and UCT"""
    if "Ovi" in Hand and "Misc" in Hand and "Archo" in DeckRem and "Pill" in DeckRem and DeckRem.count("Scraptor")>=2 and ((DeckRem.count("Baby")+DeckRem.count("Petit")>=2 and "Baby" in Hand ) or (DeckRem.count("Baby")+DeckRem.count("Petit")>=2 and "Baby" in DeckRem)) and "UCT" in DeckRem and ("Rex" in Hand or "Rex" in DeckRem):
        return True
    elif "Ovi" in Hand and "Baby" in Hand and "Misc" in DeckRem and "Archo" in DeckRem and "Pill" in DeckRem and DeckRem.count("Scraptor")>=2 and DeckRem.count("Baby")+DeckRem.count("Petit")>=2 and "UCT" in DeckRem and ("Rex" in DeckRem or "Rex" in Hand):
        return True
    elif "Misc" in Hand and ("Baby" in Hand or "Petit" in Hand) and "Archo" in DeckRem and "Ovi" in DeckRem and "Pill" in DeckRem and DeckRem.count("Scraptor")>=2 and Hand.count("Baby")+Hand.count("Petit")+DeckRem.count("Baby")+DeckRem.count("Petit")>=2 and (("UCT" in DeckRem and ("Rex" in DeckRem or "Rex" in Hand)) or ("UCT" in Hand and "Rex" in DeckRem)) and DeckRem.count("Ovi)")+DeckRem.count("Misc")+DeckRem.count("Rex")+DeckRem.count("Scraptor")>=4:
        return True
    elif "Archo" in Hand and ("Baby" in Hand or "Petit" in Hand) and "Pill" in DeckRem and "Ovi" in DeckRem and (("Misc" in Hand and DeckRem.count("Ovi")+DeckRem.count("Misc")+DeckRem.count("Rex")+DeckRem.count("Scraptor")>=4) or ("Misc" in DeckRem and DeckRem.count("Ovi")+DeckRem.count("Misc")+DeckRem.count("Rex")+DeckRem.count("Scraptor")>=5)) and ("Baby" in DeckRem or "Petit" in DeckRem) and DeckRem.count("Scraptor")>=2 and (("UCT" in DeckRem and ("Rex" in DeckRem or "Rex" in Hand)) or ("UCT" in Hand and "Rex" in DeckRem)):
        return True

def IsHandGreat(Hand,DeckRem):
    """Checks whether the hand makes full combp protected by early Dolkka with 2mat Dweller"""
    if "Archo" in Hand and "Misc" in Hand and ("Baby" in Hand or "Petit" in Hand) and "Pill" in DeckRem and "Ovi" in DeckRem and (("Rex" in DeckRem and ("UCT" in Hand or "UCT" in DeckRem)) or ("Rex" in Hand and "UCT" in DeckRem)) and ("Baby" in DeckRem or "Petit" in DeckRem) and DeckRem.count("Scraptor")>=2 and DeckRem.count("Misc")+DeckRem.count("Ovi")>=2:
        return True
    elif IsHandFullCombo(Hand,DeckRem)==True and "LostWorld" in Hand: #This is not strictly sufficient. You also need an extra baby/petit in deck to pop and an extra lvl 4 dino to summon, but I'm to lazy to write 4 lines for this
        return True
    elif IsHandFullCombo(Hand,DeckRem)==True and "Rex" in Hand and "UCT" in DeckRem: #This is not strictly speaking enough. You technically also need an extra LVL 4 Dino in Deck to summon in place of Rex
        return True
         

def IsHandInferiorCombo(Hand,DeckRem):
    """Checks whether the hand contains one of the inferior combo lines (It might still be full combo)."""
    if "Ovi" in Hand and "LostWorld" in Hand and "Misc" in DeckRem and "Baby" in DeckRem and Hand.count("Petit")+Hand.count("Baby")+DeckRem.count("Baby")+DeckRem.count("Petit")>=2 and "Pill" in DeckRem and "Archo" in DeckRem and DeckRem.count("Scraptor")>=2 and ("UCT" in Hand or "UCT" in DeckRem):
        return True
    elif "Scraptor" in Hand and "LostWorld" in Hand and "Scraptor" in DeckRem and "Baby" in DeckRem and DeckRem.count("Petit")+DeckRem.count("Baby")>=2 and "Ovi" in DeckRem and (("Misc" in DeckRem and DeckRem.count("Ovi")+DeckRem.count("Scraptor")+DeckRem.count("Rex")+DeckRem.count("Misc")>=4)or ("Misc" in Hand and DeckRem.count("Ovi")+DeckRem.count("Scraptor")+DeckRem.count("Rex")+DeckRem.count("Misc")>=3)) and "Archo" in DeckRem and "Pill" in DeckRem and ("UCT" in DeckRem or "UCT" in Hand):
        return True
    #The standard lines with less than 2 scraptors in deck belong here as well


    
def Evaluate(Hand,DeckRem):
    """Checks whether any of our levels of combo is given for a hand and deck remainder"""
    if IsHandGreat(Hand,DeckRem)==True:
        return 3

    elif IsHandFullCombo(Hand,DeckRem)==True:
       return 2

    elif IsHandInferiorCombo(Hand,DeckRem)==True:
       return 1

    else:
        return 0


def ComboChecker(DeckSize,Ovi,Misc,Baby,Petit,LostWorld,Dig,Prosperity,Archo,Pill,UCT,Rex,Scraptor):
    """Determine whether a random Start Hand of the Deck with the specified card counts has combo"""
    Deck=Misc*["Misc"]+Ovi*["Ovi"]+Baby*["Baby"]+Petit*["Petit"]+LostWorld*["LostWorld"]+Dig*["Dig"]+Prosperity*["Prosperity"]+Archo*["Archo"]+Pill*["Pill"]+UCT*["UCT"]+Rex*["Rex"]+Scraptor*["Scraptor"]
    Deck=Deck+(DeckSize-len(Deck))*["x"]
    from random import shuffle
    import copy
    shuffle(Deck)
    Hand=Deck[0:5]
    DeckRem=Deck[5:]
    PotMills=Deck[5:11]
    FossilDigTargets=["Ovi","Misc","Baby","Petit","Archo","Rex","Scraptor"]
    HandWorth=0
    if "Prosperity" in Hand:
        for i in range(0,6):
            TrialHand=copy.copy(Hand)
            TrialHand=TrialHand+[PotMills[i]]
            TrialDeckRem=copy.copy(DeckRem)
            del TrialDeckRem[i]
            if TrialHand.count("Dig")==0:
                HandWorth=max(HandWorth,Evaluate(TrialHand,TrialDeckRem))
            elif TrialHand.count("Dig")==1:
                for j in range(len(TrialDeckRem)):
                    if TrialDeckRem[j] in FossilDigTargets:
                        FinalHand=copy.copy(TrialHand)
                        FinalHand=FinalHand+[TrialDeckRem[j]]
                        FinalDeckRem=copy.copy(TrialDeckRem)
                        del FinalDeckRem[j]
                        HandWorth=max(HandWorth,Evaluate(FinalHand,FinalDeckRem))

            elif TrialHand.count("Dig")==2:
                for j in range(len(TrialDeckRem)):
                    if TrialDeckRem[j] in FossilDigTargets:
                        PreFinalHand=copy.copy(TrialHand)
                        PreFinalHand=PreFinalHand+[TrialDeckRem[j]]
                        PreFinalDeckRem=copy.copy(TrialDeckRem)
                        del PreFinalDeckRem[j]
                        for k in range(len(PreFinalDeckRem)):
                            if PreFinalDeckRem[k] in FossilDigTargets:
                                FinalHand=copy.copy(PreFinalHand)
                                FinalHand=FinalHand+[PreFinalDeckRem[k]]
                                FinalDeckRem=copy.copy(PreFinalDeckRem)
                                del FinalDeckRem[k]
                                HandWorth=max(HandWorth,Evaluate(FinalHand,FinalDeckRem))

            elif TrialHand.count("Dig")==3:
                for j in range(len(TrialDeckRem)):
                    if TrialDeckRem[j] in FossilDigTargets:
                        PrePreFinalHand=copy.copy(TrialHand)
                        PrePreFinalHand=PrePreFinalHand+[TrialDeckRem[j]]
                        PrePreFinalDeckRem=copy.copy(TrialDeckRem)
                        del PrePreFinalDeckRem[j]
                        for k in range(len(PrePreFinalDeckRem)):
                            if PrePreFinalDeckRem[k] in FossilDigTargets:
                                PreFinalHand=copy.copy(PrePreFinalHand)
                                PreFinalHand=PreFinalHand+[PrePreFinalDeckRem[k]]
                                PreFinalDeckRem=copy.copy(PrePreFinalDeckRem)
                                del PreFinalDeckRem[k]
                                for l in range(len(PreFinalDeckRem)):
                                    if PreFinalDeckRem[l] in FossilDigTargets:
                                        FinalHand=copy.copy(PreFinalHand)
                                        FinalHand=FinalHand+[PreFinalDeckRem[l]]
                                        FinalDeckRem=copy.copy(PreFinalDeckRem)
                                        del FinalDeckRem[l]
                                        HandWorth=max(HandWorth,Evaluate(FinalHand,FinalDeckRem))

    else:
        TrialHand=Hand
        TrialDeckRem=DeckRem
        if TrialHand.count("Dig")==0:
                HandWorth=max(HandWorth,Evaluate(TrialHand,TrialDeckRem))

        elif TrialHand.count("Dig")==1:
            for j in range(len(TrialDeckRem)):
                if TrialDeckRem[j] in FossilDigTargets:
                    FinalHand=copy.copy(TrialHand)
                    FinalHand=FinalHand+[TrialDeckRem[j]]
                    FinalDeckRem=copy.copy(TrialDeckRem)
                    del FinalDeckRem[j]
                    HandWorth=max(HandWorth,Evaluate(FinalHand,FinalDeckRem))

        elif TrialHand.count("Dig")==2:
            for j in range(len(TrialDeckRem)):
                if TrialDeckRem[j] in FossilDigTargets:
                    PreFinalHand=copy.copy(TrialHand)
                    PreFinalHand.append(TrialDeckRem[j])
                    PreFinalDeckRem=copy.copy(TrialDeckRem)
                    del PreFinalDeckRem[j]
                    for k in range(len(PreFinalDeckRem)):
                        if PreFinalDeckRem[k] in FossilDigTargets:
                            FinalHand=copy.copy(PreFinalHand)
                            FinalHand.append(PreFinalDeckRem[k])
                            FinalDeckRem=copy.copy(PreFinalDeckRem)
                            del FinalDeckRem[k]
                            HandWorth=max(HandWorth,Evaluate(FinalHand,FinalDeckRem))

        elif TrialHand.count("Dig")==3:
            for j in range(len(TrialDeckRem)):
                if TrialDeckRem[j] in FossilDigTargets:
                    PrePreFinalHand=copy.copy(TrialHand)
                    PrePreFinalHand.append(TrialDeckRem[j])
                    PrePreFinalDeckRem=copy.copy(TrialDeckRem)
                    del PrePreFinalDeckRem[j]
                    for k in range(len(PrePreFinalDeckRem)):
                        if PrePreFinalDeckRem[k] in FossilDigTargets:
                            PreFinalHand=copy.copy(PrePreFinalHand)
                            PrePreFinalHand.append(PrePreFinalDeckRem[k])
                            PreFinalDeckRem=copy.copy(PrePreFinalDeckRem)
                            del PreFinalDeckRem[k]
                            for l in range(len(PreFinalDeckRem)):
                                if PreFinalDeckRem[l] in FossilDigTargets:
                                    FinalHand=copy.copy(PreFinalHand)
                                    FinalHand.append(PreFinalDeckRem[l])
                                    FinalDeckRem=copy.copy(PreFinalDeckRem)
                                    del FinalDeckRem[l]
                                    HandWorth=max(HandWorth,Evaluate(FinalHand,FinalDeckRem))     



    return HandWorth
    #return HandWorth,Deck

DeckCount=41
OviCount=3
MiscCount=3
BabyCount=3
PetitCount=1
LostWorldCount=3
DigCount=3
ProsperityCount=3
ArchoCount=2
PillCount=2
UCTCount=2
RexCount=1
ScraptorCount=3

SeriesofHandWorths=[]   
for i in range(0,10000):
    
    SeriesofHandWorths.append(ComboChecker(DeckCount,OviCount,MiscCount,BabyCount,PetitCount,LostWorldCount,DigCount,ProsperityCount,ArchoCount,PillCount,UCTCount,RexCount,ScraptorCount))

print("Protected full combo: ",SeriesofHandWorths.count(3))
print("(Unprotected) Full Combo:",SeriesofHandWorths.count(2))
print("Inferior Lines (2 Rank 4s+UCT or Apo+R4+UCT):",SeriesofHandWorths.count(1))
print("Bricks (or this script is too dumb):",SeriesofHandWorths.count(0))

#print(ComboChecker(DeckCount,OviCount,MiscCount,BabyCount,PetitCount,LostWorldCount,DigCount,ProsperityCount,ArchoCount,PillCount,UCTCount,RexCount,ScraptorCount))


