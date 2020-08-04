import random
from math import floor

ALL_CARDS = ['A Thousand Cuts', 'A Thousand Cuts+1', 'Accuracy', 'Accuracy+1', 'Acrobatics', 'Acrobatics+1', 'Adaptation', 'Adaptation+1', 'Adrenaline', 'Adrenaline+1', 'After Image', 'After Image+1', 'Aggregate', 'Aggregate+1', 'All For One', 'All For One+1', 'All Out Attack', 'All Out Attack+1', 'Alpha', 'Alpha+1', 'Amplify', 'Amplify+1', 'Anger', 'Anger+1', 'Apotheosis', 'Apotheosis+1', 'Armaments', 'Armaments+1', 'AscendersBane', 'Auto Shields', 'Auto Shields+1', 'Backflip', 'Backflip+1', 'Backstab', 'Backstab+1', 'Ball Lightning', 'Ball Lightning+1', 'Bandage Up', 'Bandage Up+1', 'Bane', 'Bane+1', 'Barrage', 'Barrage+1', 'Barricade', 'Barricade+1', 'Bash', 'Bash+1', 'Battle Trance', 'Battle Trance+1', 'BattleHymn', 'BattleHymn+1', 'Beam Cell', 'Beam Cell+1', 'BecomeAlmighty', 'BecomeAlmighty+1', 'Berserk', 'Berserk+1', 'Beta', 'Beta+1', 'Biased Cognition', 'Biased Cognition+1', 'Bite', 'Bite+1', 'Blade Dance', 'Blade Dance+1', 'Blasphemy', 'Blasphemy+1', 'Blind', 'Blind+1', 'Blizzard', 'Blizzard+1', 'Blood for Blood', 'Blood for Blood+1', 'Bloodletting', 'Bloodletting+1', 'Bludgeon', 'Bludgeon+1', 'Blur', 'Blur+1', 'Body Slam', 'Body Slam+1', 'BootSequence', 'BootSequence+1', 'Bouncing Flask', 'Bouncing Flask+1', 'BowlingBash', 'BowlingBash+1', 'Brilliance', 'Brilliance+1', 'Brutality', 'Brutality+1', 'Buffer', 'Buffer+1', 'Bullet Time', 'Bullet Time+1', 'Burn', 'Burn+1', 'Burning Pact', 'Burning Pact+1', 'Burst', 'Burst+1', 'Calculated Gamble', 'Calculated Gamble+1', 'Caltrops', 'Caltrops+1', 'Capacitor', 'Capacitor+1', 'Carnage', 'Carnage+1', 'CarveReality', 'CarveReality+1', 'Catalyst', 'Catalyst+1', 'Chaos', 'Chaos+1', 'Chill', 'Chill+1', 'Choke', 'Choke+1', 'Chrysalis', 'Chrysalis+1', 'Clash', 'Clash+1', 'ClearTheMind', 'ClearTheMind+1', 'Cleave', 'Cleave+1', 'Cloak And Dagger', 'Cloak And Dagger+1', 'Clothesline', 'Clothesline+1', 'Clumsy', 'Cold Snap', 'Cold Snap+1', 'Collect', 'Collect+1', 'Combust', 'Combust+1', 'Compile Driver', 'Compile Driver+1', 'Concentrate', 'Concentrate+1', 'Conclude', 'Conclude+1', 'ConjureBlade', 'ConjureBlade+1', 'Consecrate', 'Consecrate+1', 'Conserve Battery', 'Conserve Battery+1', 'Consume', 'Consume+1', 'Coolheaded', 'Coolheaded+1', 'Core Surge', 'Core Surge+1', 'Corpse Explosion', 'Corpse Explosion+1', 'Corruption', 'Corruption+1', 'Creative AI', 'Creative AI+1', 'Crescendo', 'Crescendo+1', 'Crippling Poison', 'Crippling Poison+1', 'CrushJoints', 'CrushJoints+1', 'CurseOfTheBell', 'CutThroughFate', 'CutThroughFate+1', 'Dagger Spray', 'Dagger Spray+1', 'Dagger Throw', 'Dagger Throw+1', 'Dark Embrace', 'Dark Embrace+1', 'Dark Shackles', 'Dark Shackles+1', 'Darkness', 'Darkness+1', 'Dash', 'Dash+1', 'Dazed', 'Dazed+1', 'Deadly Poison', 'Deadly Poison+1', 'Decay', 'DeceiveReality', 'DeceiveReality+1', 'Deep Breath', 'Deep Breath+1', 'Defend', 'Defend+1', 'Deflect', 'Deflect+1', 'Defragment', 'Defragment+1', 'Demon Form', 'Demon Form+1', 'DeusExMachina', 'DeusExMachina+1', 'DevaForm', 'DevaForm+1', 'Devotion', 'Devotion+1', 'Die Die Die', 'Die Die Die+1', 'Disarm', 'Disarm+1', 'Discovery', 'Discovery+1', 'Distraction', 'Distraction+1', 'Dodge and Roll', 'Dodge and Roll+1', 'Doom and Gloom', 'Doom and Gloom+1', 'Doppelganger', 'Doppelganger+1', 'Double Energy', 'Double Energy+1', 'Double Tap', 'Double Tap+1', 'Doubt', 'Dramatic Entrance', 'Dramatic Entrance+1', 'Dropkick', 'Dropkick+1', 'Dual Wield', 'Dual Wield+1', 'Dualcast', 'Dualcast+1', 'Echo Form', 'Echo Form+1', 'Electrodynamics', 'Electrodynamics+1', 'EmptyBody', 'EmptyBody+1', 'EmptyFist', 'EmptyFist+1', 'EmptyMind', 'EmptyMind+1', 'Endless Agony', 'Endless Agony+1', 'Enlightenment', 'Enlightenment+1', 'Entrench', 'Entrench+1', 'Envenom', 'Envenom+1', 'Eruption', 'Eruption+1', 'Escape Plan', 'Escape Plan+1', 'Establishment', 'Establishment+1', 'Evaluate', 'Evaluate+1', 'Eviscerate', 'Eviscerate+1', 'Evolve', 'Evolve+1', 'Exhume', 'Exhume+1', 'Expertise', 'Expertise+1', 'Expunger', 'Expunger+1', 'FTL', 'FTL+1', 'FameAndFortune', 'FameAndFortune+1', 'Fasting2', 'Fasting2+1', 'FearNoEvil', 'FearNoEvil+1', 'Feed', 'Feed+1', 'Feel No Pain', 'Feel No Pain+1', 'Fiend Fire', 'Fiend Fire+1', 'Finesse', 'Finesse+1', 'Finisher', 'Finisher+1', 'Fire Breathing', 'Fire Breathing+1', 'Fission', 'Fission+1', 'Flame Barrier', 'Flame Barrier+1', 'Flash of Steel', 'Flash of Steel+1', 'Flechettes', 'Flechettes+1', 'Flex', 'Flex+1', 'FlurryOfBlows', 'FlurryOfBlows+1', 'Flying Knee', 'Flying Knee+1', 'FlyingSleeves', 'FlyingSleeves+1', 'FollowUp', 'FollowUp+1', 'Footwork', 'Footwork+1', 'Force Field', 'Force Field+1', 'ForeignInfluence', 'ForeignInfluence+1', 'Forethought', 'Forethought+1', 'Fusion', 'Fusion+1', 'Gash', 'Gash+1', 'Genetic Algorithm', 'Genetic Algorithm+1', 'Ghostly', 'Ghostly Armor', 'Ghostly Armor+1', 'Ghostly+1', 'Glacier', 'Glacier+1', 'Glass Knife', 'Glass Knife+1', 'Go for the Eyes', 'Go for the Eyes+1', 'Good Instincts', 'Good Instincts+1', 'Grand Finale', 'Grand Finale+1', 'Halt', 'Halt+1', 'HandOfGreed', 'HandOfGreed+1', 'Havoc', 'Havoc+1', 'Headbutt', 'Headbutt+1', 'Heatsinks', 'Heatsinks+1', 'Heavy Blade', 'Heavy Blade+1', 'Heel Hook', 'Heel Hook+1', 'Hello World', 'Hello World+1', 'Hemokinesis', 'Hemokinesis+1', 'Hologram', 'Hologram+1', 'Hyperbeam', 'Hyperbeam+1', 'Immolate', 'Immolate+1', 'Impatience', 'Impatience+1', 'Impervious', 'Impervious+1', 'Indignation', 'Indignation+1', 'Infernal Blade', 'Infernal Blade+1', 'Infinite Blades', 'Infinite Blades+1', 'Inflame', 'Inflame+1', 'Injury', 'InnerPeace', 'InnerPeace+1', 'Insight', 'Insight+1', 'Intimidate', 'Intimidate+1', 'Iron Wave', 'Iron Wave+1', 'J.A.X.', 'J.A.X.+1', 'Jack Of All Trades', 'Jack Of All Trades+1', 'Judgement', 'Judgement+1', 'Juggernaut', 'Juggernaut+1', 'JustLucky', 'JustLucky+1', 'Leap', 'Leap+1', 'Leg Sweep', 'Leg Sweep+1', 'LessonLearned', 'LessonLearned+1', 'LikeWater', 'LikeWater+1', 'Limit Break', 'Limit Break+1', 'LiveForever', 'LiveForever+1', 'Lockon', 'Lockon+1', 'Loop', 'Loop+1', 'Machine Learning', 'Machine Learning+1', 'Madness', 'Madness+1', 'Magnetism', 'Magnetism+1', 'Malaise', 'Malaise+1', 'Master of Strategy', 'Master of Strategy+1', 'MasterReality', 'MasterReality+1', 'Masterful Stab', 'Masterful Stab+1', 'Mayhem', 'Mayhem+1', 'Meditate', 'Meditate+1', 'Melter', 'Melter+1', 'MentalFortress', 'MentalFortress+1', 'Metallicize', 'Metallicize+1', 'Metamorphosis', 'Metamorphosis+1', 'Meteor Strike', 'Meteor Strike+1', 'Mind Blast', 'Mind Blast+1', 'Miracle', 'Miracle+1', 'Multi-Cast', 'Multi-Cast+1', 'Necronomicurse', 'Neutralize', 'Neutralize+1', 'Night Terror', 'Night Terror+1', 'Nirvana', 'Nirvana+1', 'Normality', 'Noxious Fumes', 'Noxious Fumes+1', 'Offering', 'Offering+1', 'Omega', 'Omega+1', 'Omniscience', 'Omniscience+1', 'Outmaneuver', 'Outmaneuver+1', 'Pain', 'Panacea', 'Panacea+1', 'Panache', 'Panache+1', 'PanicButton', 'PanicButton+1', 'Parasite', 'PathToVictory', 'PathToVictory+1', 'Perfected Strike', 'Perfected Strike+1', 'Perseverance', 'Perseverance+1', 'Phantasmal Killer', 'Phantasmal Killer+1', 'PiercingWail', 'PiercingWail+1', 'Poisoned Stab', 'Poisoned Stab+1', 'Pommel Strike', 'Pommel Strike+1', 'Power Through', 'Power Through+1', 'Pray', 'Pray+1', 'Predator', 'Predator+1', 'Prepared', 'Prepared+1', 'Pride', 'Prostrate', 'Prostrate+1', 'Protect', 'Protect+1', 'Pummel', 'Pummel+1', 'Purity', 'Purity+1', 'Quick Slash', 'Quick Slash+1', 'Rage', 'Rage+1', 'Ragnarok', 'Ragnarok+1', 'Rainbow', 'Rainbow+1', 'Rampage', 'Rampage+1', 'ReachHeaven', 'ReachHeaven+1', 'Reaper', 'Reaper+1', 'Reboot', 'Reboot+1', 'Rebound', 'Rebound+1', 'Reckless Charge', 'Reckless Charge+1', 'Recycle', 'Recycle+1', 'Redo', 'Redo+1', 'Reflex', 'Reflex+1', 'Regret', 'Reinforced Body', 'Reinforced Body+1', 'Reprogram', 'Reprogram+1', 'Riddle With Holes', 'Riddle With Holes+1', 'Rip and Tear', 'Rip and Tear+1', 'RitualDagger', 'RitualDagger+1', 'Rupture', 'Rupture+1', 'Sadistic Nature', 'Sadistic Nature+1', 'Safety', 'Safety+1', 'Sanctity', 'Sanctity+1', 'SandsOfTime', 'SandsOfTime+1', 'SashWhip', 'SashWhip+1', 'Scrape', 'Scrape+1', 'Scrawl', 'Scrawl+1', 'Searing Blow', 'Searing Blow+1', 'Second Wind', 'Second Wind+1', 'Secret Technique', 'Secret Technique+1', 'Secret Weapon', 'Secret Weapon+1', 'Seeing Red', 'Seeing Red+1', 'Seek', 'Seek+1', 'Self Repair', 'Self Repair+1', 'Sentinel', 'Sentinel+1', 'Setup', 'Setup+1', 'Sever Soul', 'Sever Soul+1', 'Shame', 'Shiv', 'Shiv+1', 'Shockwave', 'Shockwave+1', 'Shrug It Off', 'Shrug It Off+1', 'SignatureMove', 'SignatureMove+1', 'Skewer', 'Skewer+1', 'Skim', 'Skim+1', 'Slice', 'Slice+1', 'Slimed', 'Slimed+1', 'Smite', 'Smite+1', 'SpiritShield', 'SpiritShield+1', 'Spot Weakness', 'Spot Weakness+1', 'Stack', 'Stack+1', 'Static Discharge', 'Static Discharge+1', 'Steam', 'Steam Power', 'Steam Power+1', 'Steam+1', 'Storm', 'Storm of Steel', 'Storm of Steel+1', 'Storm+1', 'Streamline', 'Streamline+1', 'Strike', 'Strike+1', 'Study', 'Study+1', 'Sucker Punch', 'Sucker Punch+1', 'Sunder', 'Sunder+1', 'Survivor', 'Survivor+1', 'Sweeping Beam', 'Sweeping Beam+1', 'Swift Strike', 'Swift Strike+1', 'Swivel', 'Swivel+1', 'Sword Boomerang', 'Sword Boomerang+1', 'Tactician', 'Tactician+1', 'TalkToTheHand', 'TalkToTheHand+1', 'Tantrum', 'Tantrum+1', 'Tempest', 'Tempest+1', 'Terror', 'Terror+1', 'The Bomb', 'The Bomb+1', 'Thinking Ahead', 'Thinking Ahead+1', 'ThirdEye', 'ThirdEye+1', 'ThroughViolence', 'ThroughViolence+1', 'Thunder Strike', 'Thunder Strike+1', 'Thunderclap', 'Thunderclap+1', 'Tools of the Trade', 'Tools of the Trade+1', 'Transmutation', 'Transmutation+1', 'Trip', 'Trip+1', 'True Grit', 'True Grit+1', 'Turbo', 'Turbo+1', 'Twin Strike', 'Twin Strike+1', 'Underhanded Strike', 'Underhanded Strike+1', 'Undo', 'Undo+1', 'Unload', 'Unload+1', 'Uppercut', 'Uppercut+1', 'Vault', 'Vault+1', 'Vengeance', 'Vengeance+1', 'Venomology', 'Venomology+1', 'Vigilance', 'Vigilance+1', 'Violence', 'Violence+1', 'Void', 'Void+1', 'Wallop', 'Wallop+1', 'Warcry', 'Warcry+1', 'WaveOfTheHand', 'WaveOfTheHand+1', 'Weave', 'Weave+1', 'Well Laid Plans', 'Well Laid Plans+1', 'WheelKick', 'WheelKick+1', 'Whirlwind', 'Whirlwind+1', 'White Noise', 'White Noise+1', 'Wild Strike', 'Wild Strike+1', 'WindmillStrike', 'WindmillStrike+1', 'Wireheading', 'Wireheading+1', 'Wish', 'Wish+1', 'Worship', 'Worship+1', 'Wound', 'Wound+1', 'Wraith Form v2', 'Wraith Form v2+1', 'WreathOfFlame', 'WreathOfFlame+1', 'Writhe', 'Zap', 'Zap+1']
ALL_RELICS = ['Akabeko', 'Anchor', 'Ancient Tea Set', 'Art of War', 'Astrolabe', 'Bag of Marbles', 'Bag of Preparation', 'Bird Faced Urn', 'Black Blood', 'Black Star', 'Blood Vial', 'Bloody Idol', 'Blue Candle', 'Boot', 'Bottled Flame', 'Bottled Lightning', 'Bottled Tornado', 'Brimstone', 'Bronze Scales', 'Burning Blood', 'Busted Crown', 'Cables', 'Calipers', 'Calling Bell', 'CaptainsWheel', 'Cauldron', 'Centennial Puzzle', 'CeramicFish', 'Champion Belt', "Charon's Ashes", 'Chemical X', 'CloakClasp', 'ClockworkSouvenir', 'Coffee Dripper', 'Cracked Core', 'CultistMask', 'Cursed Key', 'Damaru', 'Darkstone Periapt', 'DataDisk', 'Dead Branch', 'Dodecahedron', 'DollysMirror', 'Dream Catcher', 'Du-Vu Doll', 'Ectoplasm', 'Emotion Chip', 'Empty Cage', 'Enchiridion', 'Eternal Feather', 'FaceOfCleric', 'FossilizedHelix', 'Frozen Egg 2', 'Frozen Eye', 'FrozenCore', 'Fusion Hammer', 'Gambling Chip', 'Ginger', 'Girya', 'Golden Idol', 'GoldenEye', 'Gremlin Horn', 'GremlinMask', 'HandDrill', 'Happy Flower', 'HolyWater', 'HornCleat', 'HoveringKite', 'Ice Cream', 'Incense Burner', 'InkBottle', 'Inserter', 'Juzu Bracelet', 'Kunai', 'Lantern', "Lee's Waffle", 'Letter Opener', 'Lizard Tail', 'Magic Flower', 'Mango', 'Mark of Pain', 'Mark of the Bloom', 'Matryoshka', 'MawBank', 'MealTicket', 'Meat on the Bone', 'Medical Kit', 'Melange', 'Membership Card', 'Mercury Hourglass', 'Molten Egg 2', 'Mummified Hand', 'MutagenicStrength', 'Necronomicon', 'NeowsBlessing', "Nilry's Codex", 'Ninja Scroll', "Nloth's Gift", 'NlothsMask', 'Nuclear Battery', 'Nunchaku', 'Odd Mushroom', 'Oddly Smooth Stone', 'Old Coin', 'Omamori', 'OrangePellets', 'Orichalcum', 'Ornamental Fan', 'Orrery', "Pandora's Box", 'Pantograph', 'Paper Crane', 'Paper Frog', 'Peace Pipe', 'Pear', 'Pen Nib', "Philosopher's Stone", 'Pocketwatch', 'Potion Belt', 'Prayer Wheel', 'PreservedInsect', 'PrismaticShard', 'PureWater', 'Question Card', 'Red Mask', 'Red Skull', 'Regal Pillow', 'Ring of the Serpent', 'Ring of the Snake', 'Runic Capacitor', 'Runic Cube', 'Runic Dome', 'Runic Pyramid', 'SacredBark', 'Self Forming Clay', 'Shovel', 'Shuriken', 'Singing Bowl', 'SlaversCollar', 'Sling', 'Smiling Mask', 'Snake Skull', 'Snecko Eye', 'Sozu', 'Spirit Poop', 'SsserpentHead', 'StoneCalendar', 'Strange Spoon', 'Strawberry', 'StrikeDummy', 'Sundial', 'Symbiotic Virus', 'TeardropLocket', 'The Courier', 'The Specimen', 'TheAbacus', 'Thread and Needle', 'Tingsha', 'Tiny Chest', 'Tiny House', 'Toolbox', 'Torii', 'Tough Bandages', 'Toxic Egg 2', 'Toy Ornithopter', 'TungstenRod', 'Turnip', 'TwistedFunnel', 'Unceasing Top', 'Vajra', 'Velvet Choker', 'VioletLotus', 'War Paint', 'WarpedTongs', 'Whetstone', 'White Beast Statue', 'WingedGreaves', 'WristBlade', 'Yang']
ALL_ENCOUNTERS = ['2 Fungi Beasts', '2 Louse', '2 Orb Walkers', '2 Thieves', '3 Byrds', '3 Cultists', '3 Darklings', '3 Louse', '3 Sentries', '3 Shapes', '4 Byrds', '4 Shapes', 'Apologetic Slime', 'Automaton', 'Awakened One', 'Blue Slaver', 'Book of Stabbing', 'Centurion and Healer', 'Champ', 'Chosen', 'Chosen and Byrds', 'Collector', 'Colosseum Nobs', 'Colosseum Slavers', 'Cultist', 'Cultist and Chosen', 'Donu and Deca', 'Exordium Thugs', 'Exordium Wildlife', 'Flame Bruiser 1 Orb', 'Flame Bruiser 2 Orb', 'Giant Head', 'Gremlin Gang', 'Gremlin Leader', 'Gremlin Nob', 'Hexaghost', 'Jaw Worm', 'Jaw Worm Horde', 'Lagavulin', 'Lagavulin Event', 'Large Slime', 'Looter', 'Lots of Slimes', 'Masked Bandits', 'Maw', 'Mind Bloom Boss Battle', 'Mysterious Sphere', 'Nemesis', 'Orb Walker', 'Red Slaver', 'Reptomancer', 'Sentry and Sphere', 'Shell Parasite', 'Shelled Parasite and Fungi', 'Shield and Spear', 'Slaver and Parasite', 'Slavers', 'Slime Boss', 'Small Slimes', 'Snake Plant', 'Snecko', 'Snecko and Mystics', 'Snecko and Mystics', 'Sphere and 2 Shapes', 'Spheric Guardian', 'Spire Growth', 'The Eyes', 'The Guardian', 'The Heart', 'The Mushroom Lair', 'Time Eater', 'Transient', 'Writhing Mass']

ACT = ['HALLWAY', 'HALLWAY', 'NOOP', 'HALLWAY', 'REST', 'ELITE', 'REST', 'HALLWAY', 'NOOP', 'HALLWAY', 'ELITE', 'HALLWAY', 'NOOP', 'HALLWAY', 'REST', 'BOSS', 'MEGA_REST']
MAP = ACT + ACT + ACT

CARD_OFFSET = 4
RELIC_OFFSET = 4 + len(ALL_CARDS)
LAST_FLOOR = len(MAP)
MAX_HP = 80
ASCENSION = 0

class Game():
    """
    This class specifies the base Game class. To define your own game, subclass
    this class and implement the functions below.
    """
    def __init__(self):
        pass

    def encode_list(list_to_encode, category):
        np_array = np.array(list_to_encode)
        encoder = OneHotEncoder(categories=[category], sparse=False)
        n_by_1 = np_array.reshape(len(np_array), 1)
        onehot_encoded = encoder.fit_transform(n_by_1)
        summed = np.sum(onehot_encoded, axis=0)
        return summed

    def get_max_hp(self, board):
        return board[0]

    def get_cur_hp(self, board):
        return board[1]
        
    def get_floor(self, board):
        return board[2]
        
    def get_ascension(self, board):
        return board[3]

    def getInitBoard(self):
        """
        Returns:
            startBoard: a representation of the board (ideally this is the form
                        that will be the input to your neural network)
        """
        board = np.zeroes(self.getBoardSize())
        board[0] = MAX_HP
        board[1] = MAX_HP
        board[2] = 0
        board[3] = ASCENSION
        board[CARD_OFFSET + ALL_CARDS.index("Strike")] = 5
        board[CARD_OFFSET + ALL_CARDS.index("Defend")] = 4
        board[CARD_OFFSET + ALL_CARDS.index("Bash")] = 1
        board[RELIC_OFFSET + ALL_RELICS.index("Burning Blood")] = 1
        pass

    def getBoardSize(self):
        """
        Returns:
            (x,y): a tuple of board dimensions
        """
        return (4 + len(ALL_CARDS) + len(ALL_RELICS), 1)

    def getActionSize(self):
        """
        Returns:
            actionSize: number of all possible actions
        """
        # the number of cards (since these are what we can pick) or skip
        return len(ALL_CARDS) + 1

    def getNextState(self, board, action):
        """
        Input:
            board: current board
            action: action taken by current player
        Returns:
            nextBoard: board after applying action
        """
        nextBoard = board.copy()
        # action >= len(ALL_CARDS) means a skip
        if action < len(ALL_CARDS):
            nextBoard[CARD_OFFSET + action] += 1
        nextBoard[2] += 1 # go up a floor
            
        # simulate the user taking damage in the current combat encounter and moving onto the next room
        floor = self.get_floor(board)
        if floor < LAST_FLOOR:
            room_type = MAP[floor]
            if room_type == 'REST':
                cur_hp = self.get_cur_hp()
                cur_hp += 0.3 * self.get_max_hp()
                nextBoard[1] = min(floor(cur_hp), self.get_max_hp()) # rest sites heal hitpoints
            elif room_type == 'MEGA_REST':
                nextBoard[1] = self.get_max_hp()
            # yeah just fake it for a moment until I plug it into the actual slay-I and pick encounters
            # this is actually useless though since it means the model cant learn anything
            elif room_type == 'HALLWAY':
                cur_hp = self.get_cur_hp()
                nextBoard[1] = cur_hp - 3
            elif room_type == 'ELITE':
                cur_hp = self.get_cur_hp()
                nextBoard[1] = cur_hp - 10
            elif room_type == 'BOSS':
                cur_hp = self.get_cur_hp()
                nextBoard[1] = cur_hp - 20
        
        return nextBoard

    def getValidMoves(self, board):
        """
        Input:
            board: current board
        Returns:
            validMoves: a binary vector of length self.getActionSize(), 1 for
                        moves that are valid from the current board,
                        0 for invalid moves
        """
        
        # begin with all card choices as invalid
        valid_mask = np.zeros(len(ALL_CARDS) + 1)
        
        # only can make card choices on floors with fights
        floor = self.get_floor(board)
        if floor < LAST_FLOOR:
            room_type = MAP[floor]
            if room_type == 'HALLWAY' or 'ELITE' or 'BOSS':
                # make three card choices valid
                valid_set = {}
                while len(valid_set) < 3:
                    valid_set.add(random.randrange(0, len(valid_mask)))
                for pos in valid_set:
                    valid_mask[pos] = 1
            
        # skip is always valid
        valid_mask[len(ALL_CARDS)] = 1
        
        return valid_mask
            

    def getGameEnded(self, board):
        """
        Input:
            board: current board
        Returns:
            r: 0 if game has not ended. 1 if player won, -1 if player lost.
               
        """
        if get_cur_hp(board) <= 0:
            return -1
        elif get_floor(board) >= LAST_FLOOR:
            return 1
        else:
            return 0

    def stringRepresentation(self, board):
        """
        Input:
            board: current board
        Returns:
            boardString: a quick conversion of board to a string format.
                         Required by MCTS for hashing.
        """
        return ":".join(board)