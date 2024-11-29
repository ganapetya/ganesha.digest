from transformers import pipeline

# Choose a supported summarization model (e.g., T5)
model_name = "t5-base"

# Create the summarization pipeline
summarizer = pipeline("summarization", model=model_name, device=0)
text=""" 
Putin’s threats became even fiercer this month after the Biden administration finally gave Kyiv permission to launch longer-range American weapons at targets deep inside Russia. In response, Putin updated Russia’s nuclear doctrine and fired a new, nuclear-capable ballistic missile at Ukraine. The message was taken as a clear threat to Ukraine’s backers: Don’t test us.

But, nearly three years into the war, these developments have assumed a familiar rhythm. Each time Ukraine made a request – first asking for tanks, then fighter jets, then cluster munitions, then long-range weapons – its allies agonized over whether to grant it, fearing it would escalate the conflict and provoke a Russian responsei.

Each time, when the West finally accepted Ukraine’s requests, Russia’s most catastrophic threats did not materialize. What was taboo one week became normal the next.

Despite Putin’s heightened threats since the latest taboo crumbled, there is little reason to believe that this time will be different, analysts told CNN.

Instead, they said the anxious reaction to Ukraine’s newly granted powers is another example of the Kremlin’s successful strategy of forcing the West to see the conflict on Russia’s terms, confusing each fresh attempt by Ukraine to resist Russian aggression as a major “escalation.”

Alongside the battlefields, the Kremlin has been engaged in a fight to force the West to argue from Russian premises rather than its own, and to “make decisions in that Kremlin-generation alternative reality that will allow Russia to win in the real world,” the Institute for the Study of War (ISW), a think-tank, said in a report in March.

Kateryna Stepanenko, a co-author of that report, told CNN the strategy was a revival of the Soviet concept “reflexive control,” by which a state imposes a false set of choices on its adversary, forcing the adversary to make decisions against its own interests.

“The persistent Western debates and delays in Western military aid to Ukraine is a clear example of the Kremlin’s successful reflexive control strategy, which had committed the Western to self-deterrence despite routine Russian escalations of the war,” Stepanenko said.

This strategy could be seen in action on Thursday after Russia launched a large-scale attack targeting Ukraine’s power grid. Although Putin said the attack was “a response from our side” to the Biden administration’s decision on longer-range weapons, Russia has not needed a pretext for such strikes in the past.

"""

text2="""

The Biden administration sent US-made Army Tactical Missile Systems, or ATACMS, to Ukraine earlier this year, but placed strict conditions on how they could be used: They could be fired at Russian targets in occupied Ukraine, but not on Russia’s own territory.

William Alberque, a former director of NATO’s Arms Control, Disarmament, and WMD Non-Proliferation Centre, said this policy made little sense – and was to Russia’s huge benefit.

By providing Ukraine with ATACMS but only allowing it to strike parts of Ukraine occupied by Russia, “we sent Russia the message: ‘You know what? If you just move a couple meters over that border, you’re safe as houses,’” Alberque told CNN.

“I’m sure the Russian commanders couldn’t believe their luck. ‘So if I set up my command headquarters here, they’ll blow me up, but if I set up a kilometer away, I’m fine? Really? Awesome!’”

In effect, this policy led to “the idea that Russia can kill anyone anywhere in Ukraine, but Ukraine can’t kill the troops that are actually attacking them if they’re across the border (in Russia).” This idea is “nonsense,” Alberque said.

Ukraine’s actions remain within the laws of armed conflict. As Poland’s Foreign Minister Radek Sikorski put it to CNN in September, “the victim of aggression has the right to defend itself also on the territory of the aggressor.”

Amid the anxious responses to last week’s developments, it is easy to forget that Ukraine has long launched home-grown drones at targets extremely deep in Russia – and that it had already fired Western weapons at territory the Kremlin considers its own. The decision to fire slightly longer-range Western weapons is a difference of degree, not of kind.

For more than a year, Kyiv has used British Storm Shadows to strike Crimea, which Russia has occupied since 2014. For months, Kyiv has been allowed to fire ATACMS at Russian targets in occupied Ukraine. By law, Russia considers these territories its own, and warned of dire consequences if Ukraine targeted them with Western weaponry.

"""

# Generate the summary
summary = summarizer(text2)

print(summary[0]['summary_text'])
