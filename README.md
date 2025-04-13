# Forgotten-Forrest
Map:
[Forest Entrance]
       ↓
  [Mossy Path]
       ↓
 [Fork in the Road]
    ↙        ↘
[Cabin]     [Dark Cave]
                ↓
         [Hidden Exit]

Goal - You’ve woken up in a strange forest with no memory of how you got there. Your goal is to find your way out while surviving creatures, traps, and solving puzzles.

Key Features to Code:
- Dictionary to hold room descriptions and options;
- Loop for navigating the world;
- Functions for player choices and consequences;
- inventory = [] to store found items.

1. Forest Entrance (Starting Point)
Description:
You wake up on damp moss with fog creeping along the ground. Trees tower above you, blocking the sun. You hear distant whispers and a crow caws overhead.
What Happens:
Player must decide to go forward or wait.
If they wait, a shadowy figure is glimpsed but vanishes (a subtle foreshadowing event)
Going forward triggers the start of the journey.
Possible Item: A branch (can be used later as a torch handle or weapon).

2. Mossy Path
Description:
The path is slippery and lined with strange, glowing mushrooms. A small stream cuts across the trail.
What Happens:
Player hears rustling in the bushes.
Option 1: Investigate (find a wounded animal or get attacked by a wild boar.
Option 2: Ignore and continue
A small puzzle appears: how to cross the stream safely (jump over? build a path with stones?)
Item: Can find glowing mushrooms (used later in the dark cave if you don’t have a torch).
Optional Danger: Lose some health if you fall into the stream.

3. Fork in the Road
Description:
A wooden signpost points in two directions:
Left: "Shelter"
Right: "Darkness"
The sign is scratched and weathered—someone tried to alter the wording.
What Happens:
The player chooses their path.
Left to the Cabin
Right to the Dark Cave
Item: A strange note on the ground:
“Trust the shelter, but check the shadows.”

4. Abandoned Cabin
Description:
An old wooden cabin stands silently. Windows are shattered, and the door creaks open. Inside, it's dusty and cluttered with old survival gear.
What Happens:
Player explores the cabin:
Find a rusty key
Light a torch using the fireplace if they have a stick
Discover a journal hinting at someone else trying to escape
Spooky Moment: If the player stays too long, they hear heavy footsteps outside.
Puzzle: Break open a locked chest using tools or a clever trick.

5. Dark Cave
Description:
Pitch black. The walls drip with moisture. Strange etchings glow faintly.
What Happens:
Requires light source (torch or glowing mushrooms), or the player gets lost/injured.
Puzzle: navigate a maze-like sequence (can be random or based on memory).
Hidden danger: cave bats or a bear (if noise is made)
Use the rusty key from the Cabin to unlock a gate deep in the cave.
Outcome: Unlocking the gate leads to the Hidden Exit.

6. Hidden Exit
Description:
You find a carved stone doorway overgrown with vines. It leads to a sunlit meadow.
What Happens:
Game ends with player escaping
Optional endings:
Good ending: Player escapes with full health and all clues
Neutral ending: Escapes but didn’t uncover full story
Bad ending: Gets lost or attacked because of a bad choice

Optional Systems:
Health (start with 100, lose 10–30 with bad choices)
Inventory (torch, mushrooms, key, journal, etc.)
Mystery Lore: Pieced together from journal entries, carvings, and notes

The Spooky Man – Side Story Arc
“You never see him clearly. You only hear him. Or catch the outline. But he always seems to know where you are.”
First Encounter – Forest Entrance
After a few moments of silence, you hear a low whisper behind you. You spin around—nothing. But a faint set of footprints in the mud weren’t there before...
If the player stays too long without moving forward, a "shadow" flickers across the screen.
Flavor text:
“Something tall. Watching. Gone before you can blink.”
Second Encounter – Mossy Path
As the player crosses the stream, they spot something in the water: a black hat drifting past. It's old. Torn. Still wet.
If they investigate, they see no one, but gain an item: Old Hat (you can make this optional).
If they pick it up, sometimes at random future events, they hear footsteps that stop when they turn.
Third Encounter – Fork in the Road
If the player examines the post closely:
“There’s something scratched just below the arrows. A warning?”
“He waits in the dark, but the fire makes him flee.”
This is a hint that the Spooky Man is afraid of light.
Cabin Clue
Inside the locked chest (if the player opens it), they find:
A torn journal page:
“He walks without breath. I stayed by the fire and he vanished. But the others—he took them in the night. He only comes when it’s quiet…”
And scratched on the walls of the cabin:
“Do not let the fire die.”
If the player lets their torch go out later in the game (like inside the cave), that’s when...
Final Encounter – Cave (Bad Path)
If the player enters the cave without a torch or light source:
The air grows colder. You hear breathing, but it's not yours.
A faint outline in the dark. Eyes? No... two glowing white slits.
You can’t move.
“You shouldn’t have come in the dark,” a voice rasps from nowhere.
If the player has light → the figure disappears with a screech.
If not → the game ends with a bad ending:
“You were never seen again. But now, another Old Hat floats by the stream.”
Who is the Spooky Man?
Let it stay vague, but plant theories:
Is he a previous explorer who got trapped?
A forest spirit guarding the path?
A hallucination from the mushrooms?

The Lost Explorer – Side Story #2
“She came before you. Brave. Prepared. Determined to map the forest and find a way out. But something went wrong. All that's left are the things she dropped... and her last messages.”
Who is She?
Eira, a young explorer who entered the forest weeks ago.
She left clues behind — journal pages, sketched maps, and personal items.
Optional side goal: Reconstruct her journey by finding her scattered belongings.
Clue System:
You can make this optional but rewarding — if the player finds all of Eira’s clues, they get:
The good ending
Or an optional alternate escape route not shown on the main path
Or a final scene where you “set her spirit free” (if you want a mystical twist)
1. Mossy Path – First Clue
A torn piece of paper, caught on a branch.
Contains a sketch of the forest entrance and a note:
“I marked the safe paths with moss bundles. Don’t trust the signs.”
Also includes a drawing of a person in a wide-brim hat, crossed out.
“He followed me too...”
2. Fork in the Road – Eira’s Compass
A broken compass lies half-buried in the dirt.
If picked up, it sometimes points toward hidden secrets (you can simulate this with random chance of bonus finds in future rooms).
Inspecting it shows a note scratched on the back:
“The cave entrance was hidden. Found it by accident. Could be a way out... if I survive it.”
3. Cabin – Her Shelter
Inside the cabin, behind a loose plank, the player finds a partially-burned journal.
"The fire keeps him away. I see him less when it burns high...
But I’m tired. So tired. If anyone finds this — don’t let your light go out.”
Lore hint: She may have faced the Spooky Man too. Her torch saved her for a while.
Also in the journal:
“There’s another path. Past the cave. Through the waterfall...”
This opens the idea for a hidden ending — if you follow Eira’s clues, you escape through a secret passage behind a waterfall, not the usual path.
4. Cave – The Final Message
Scratched into the wall of the cave:
“I made it through. I think. There’s a light ahead.
I’m leaving this for the next one. You. Be smarter than I was.”
At the cave exit:
An old pendant on the ground — Eira’s final belonging
Player can take it (honor her) or leave it (somehow this changes the final scene slightly)
Optional Endings Based on This Side Story:
All Clues Found → player unlocks the waterfall escape route
Some Clues → player sees a vision of Eira smiling before exiting, like her spirit is at peace
No Clues → nothing changes, but lore is missed
Intertwining with the Spooky Man
Even cooler — if the player finds both storylines, you can hint that:
Eira and the Spooky Man might be connected (he was her mentor, brother, or… her transformed self?)
Or it was Eira who became the Spooky Man after being trapped in the dark too long (if you want a twist)

Side Story #3: The Whispering Tree
"There’s a tree in the forest. It’s ancient. It listens. Sometimes it speaks back."
— Unknown
This one adds a mythical, creepy-natural twist — not ghosts, not people, but the forest itself being alive and maybe conscious.
What Is the Whispering Tree?
A giant, moss-covered tree hidden deep in the forest.
It “whispers” things — sometimes useful, sometimes lies.
Players can choose to trust or ignore it.
It could give:
Cryptic hints about puzzles or paths
Warnings about the Spooky Man
Weird, unsettling phrases that mess with the player’s head 
How to Build It In:
When do you encounter it?
Maybe tucked away after the Fork in the Road, behind a small overgrown side path.
You hear the whisper before you see it:
“This way… left is light, but right is truth…”
The Interaction
Let the player choose to:
Touch the tree (you gain a "mark" that alters some outcomes)
Listen longer (get a hint — or a lie)
Carve into the bark (anger it )
Then later, if the player has the mark:
The Spooky Man hesitates before attacking
The Cave “recognizes” you and opens a secret passage
OR the tree whispers your name later (creepy but awesome)
Connection to the Other Stories:
Eira’s journal could mention the tree:
“It told me to leave the path. I didn’t. Now I wonder… what if?”
The Spooky Man avoids the tree. He never goes near it.
One theory: the tree is the forest’s guardian — ancient and neutral.
What It Adds:
Myth and mystery
More freedom of choice (trust the whispers? ignore them?)
A slightly magical or otherworldly feeling that adds depth without clutter
Lies (to trick or confuse):
“The cave is your salvation.”
(Even if they’re unprepared — leads to danger.)
“The man in the hat is your friend.”
“You’ve already been here. You just don’t remember.”
“Eira found peace in the dark.”
(She didn’t.)
“Burn the journal. Set yourself free.”
“There is no exit. Only roots.”
Truths (helpful, but vague):
“The fire is your shield. Feed it.”
“Moss covers safety. Where the moss grows thick, danger does not.”
“He fears the light. He flees the warmth.”
“The pendant is more than it seems.”
(Eira’s pendant could alter the ending.)
“You are not the first.”
“A waterfall hides what stone forgets.”
(Clue to secret exit.)
Eerie Ambiguity (neither true nor false, just creepy):
“Your shadow walks faster than you.”
“The roots remember your name.”
“Something walks when you stop. Something stops when you walk.”
“You are being watched. But not by what you fear.”
“You will return here, even if you don’t leave.”
“The forest took her, but left her voice.”
“The trees forget, but the stones... never do.”
Clue Format Ideas:
You can randomize the tree's sayings each time the player interacts.
Optionally, if the player has a certain item (like Eira’s journal), the tree could whisper something different — like:
“Ah. You carry her burden.”
You could even include progressive whispers (one for each visit) to encourage backtracking and deepen the mystery.
