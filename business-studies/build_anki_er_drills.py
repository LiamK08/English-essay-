#!/usr/bin/env python3
"""Build the ER Paragraph Drills Anki deck (.apkg).

19 requested terms x 3 cards each (Define / Build / Qantas), mirroring the
define -> build -> Qantas paragraph structure of the extended response.
Content mirrors business-studies/operations-extended-response-notes.md.
"""
import genanki

MODEL = genanki.Model(
    1607392319,
    'Operations ER (Basic)',
    fields=[{'name': 'Front'}, {'name': 'Back'}],
    templates=[{
        'name': 'Card 1',
        'qfmt': '<div class="q">{{Front}}</div>',
        'afmt': '{{FrontSide}}<hr id="answer"><div class="a">{{Back}}</div>',
    }],
    css="""
.card { font-family: -apple-system, Segoe UI, Arial, sans-serif; font-size: 19px;
        text-align: left; color: #1a1a1a; background-color: #fdfdfd; padding: 14px; }
.q { font-weight: 600; }
.a { margin-top: 6px; }
b { color: #b30000; }
.tag { display:inline-block; font-size: 13px; font-weight: 700; color:#fff;
       background:#8a0e0e; border-radius: 4px; padding: 1px 7px; margin-bottom: 6px; }
.tag.build { background:#0e5a8a; }
.tag.qantas { background:#8a5a0e; }
ul { margin: 4px 0 4px 18px; padding: 0; }
li { margin: 3px 0; }
.night_mode .card { color:#eee; background-color:#2b2b2b; }
.night_mode b { color:#ff8080; }
""")

DECK = genanki.Deck(2059400114,
                    'Operations ER::5. ER Paragraph Drills (Define · Build · Qantas)')

DEF = '<span class="tag">DEFINE</span><br>'
BLD = '<span class="tag build">BUILD — characteristics &amp; features</span><br>'
QAN = '<span class="tag qantas">QANTAS RELEVANCE</span><br>'

# term: (definition, build, qantas)
TERMS = {
 'Globalisation': (
  '"Globalisation refers to the <b>removal of barriers of trade between nations</b>… characterised by an increasing integration between national economies and a high degree of transfer of capital, labour, intellectual capital and ideas, financial resources and technology."<br><br>Simpler: the increasing interconnection and interdependence of global businesses and markets.',
  '<ul><li>Affects every input: <b>materials</b> (cheaper globally sourced), <b>labour</b> (cheaper overseas), <b>facilities</b> (offshore factories/tech), <b>customers</b> (bigger markets, different cultures → customisation), <b>competition</b> (overseas cost advantages), <b>finance</b> (cheaper global funds).</li><li>Key terms: <b>supply chain</b> (range of suppliers + relationships) and <b>global web</b> (suppliers chosen on lowest cost, lowest risk, maximum certainty).</li><li>Process link: impacts <b>inputs</b> (global resources), <b>transformation</b> (4 V\'s, task design, sequencing, technology, layout) and <b>outputs</b> (global reach, customisation, distribution efficiency).</li><li>Answered through: global factors, SCM, outsourcing.</li></ul>',
  '<ul><li><b>+220,000 international seats FY25</b>; 2025 capacity of 7.1M seats is 2.5% above pre-COVID.</li><li>International revenue <b>$8.7bn FY24</b>; 70% of assets global-facing, 50% Asia-focused.</li><li>Competition: <b>62 international airlines in 2024 vs 52 in 2000</b>; 70% of the 40 airlines serving Australia get home-government support — Qantas does not.</li><li><b>Oneworld</b>: 900 destinations, 170+ countries; Emirates partnership (Dubai hub cuts costs).</li></ul>'),
 'Supply chain management': (
  '"SCM involves <b>integrating and managing the flow of supplies throughout the inputs, transformation processes and outputs</b> in order to best meet the needs of customers." (The definition itself is the process link — quote it.)',
  '<ul><li>Three aspects: <b>logistics</b>, <b>e-commerce</b>, <b>global sourcing</b>.</li><li>Suppliers must deliver the right inputs at the <b>best price, reliably, in the required quantity and quality</b>.</li><li><b>Lead time</b> (order → delivery) determines how flexible operations can be.</li><li>An effective supply chain must respond to demand changes — breaks in production waste costs.</li></ul>',
  '<ul><li>~<b>10,000 supply partners, ~$12 billion annual spend</b>.</li><li>Direct fuel pipeline <b>Kurnell refinery → Sydney Airport</b> (750M litres storage); 22,500 sqm Mascot distribution centre.</li><li><b>97% of sales online</b>, ~70% of bookings via the app/site.</li><li>SAF sourced from London (BP) and <b>California (20M litres p.a. from 2025 — FY25)</b>; all aircraft bought globally in USD.</li></ul>'),
 'Technology (influence)': (
  '"Technology is the <b>design, construction and/or application of innovative devices, methods and machinery</b> upon operations processes."',
  '<ul><li><b>Administrative level</b>: planning tech (Gantt charts, CPA), office + software tech → "assist with organisation, planning and decision making to help <b>control</b> the operational processes."</li><li><b>Processing level</b>: machinery, robotics, CAD, CAM, CIM → "improve <b>accuracy, speed and efficiency</b> of production and therefore improved outputs."</li><li>Adopting adequate technology is <b>essential to stay competitive</b> in a digital era — automates tasks, cuts costs, gives data-driven insights.</li><li>Answered through the technology strategy (leading edge vs established).</li></ul>',
  '<ul><li><b>$230M</b> digital/customer investment FY24; <b>RFID baggage tracking</b> cut mishandled bags <b>30%</b> FY24 vs FY23.</li><li><b>28 A321XLRs delivered 2025 (FY25)</b> — ~17% less fuel, +15% passengers; 787-9 burns 20% less fuel per seat than the 747.</li><li><b>Constellation</b> AI weather-tracking saves 2% fuel/yr; FlightPulse avoided 5.71M kg CO2 in year one.</li><li>240 Sydney kiosks cut check-in times up to <b>90%</b>; free international Wi-Fi rollout from late 2024.</li></ul>'),
 'Quality expectations': (
  '"Quality expectations refers to the <b>influence that consumers have on a business</b>, as their expectations for a product will determine the way in which that product is <b>designed, created and delivered</b>."',
  '<ul><li><b>Goods</b>: quality of design, fit for purpose, durability.</li><li><b>Services</b>: professionalism, reliability, level of customisation.</li><li>Australian expectations are high — stringent standards, consumer protection laws, industry regulation.</li><li>Process link: shapes design, production and delivery → drives <b>monitoring, control and improvement</b> and output quality. Classic strategy pairing: <b>quality management</b> (control/assurance/improvement + TQM).</li></ul>',
  '<ul><li>OTP <b>80%</b> in Q4 FY24 (Jetstar 74%); Q4 FY24 OTP +10 pts / NPS +22 pts vs Q2; domestic NPS <b>+24 points FY24</b>.</li><li><b>$100M lounge investment</b> (42 domestic + 9 international) FY24.</li><li>4-star Skytrax; <b>#2 safest airline in the world 2025</b> (Airline Ratings).</li><li>The warning: customer trust fell <b>74% → 47%</b> (2023→24) — unmet expectations punish reputation.</li></ul>'),
 'Cost-based competition': (
  '"Cost-based competition is derived from determining the <b>breakeven point (TC = TR)</b> and then applying strategies to create <b>cost advantages over competitors</b>."',
  '<ul><li>If a competitor cuts prices, operations must cut costs: cheaper inputs, better efficiency, smaller product range.</li><li>Five cost levers: <b>eliminate waste, bulk-buy, high-volume output, automation, economies of scale</b>.</li><li>The tension: cut costs <b>without compromising quality</b> — crucial in price-sensitive markets.</li><li>Process link: cheaper inputs + efficient/automated transformation + high-volume outputs → lower cost per unit.</li></ul>',
  '<ul><li>Cut <b>$5 billion over 6 years</b> (cost base −20%); further <b>$400M cost-out planned for 2025 (FY25)</b>.</li><li>Unit cost <b>9.73c/ASK FY24, down 4.5%</b> from 10.19c.</li><li><b>Jetstar</b>: 11 million fares under $100 sold FY24.</li><li>Cost structure: staff 26%, aircraft operating 23%, fuel 22%.</li></ul>'),
 'Government policies': (
  '"Government policies are <b>methods used by government that encourage the operations function to be more innovative and competitive</b>, as it ultimately produces more income for the nation."',
  '<ul><li>Policy areas: <b>taxation, WHS, public health, environment, employment relations, trade</b>.</li><li><b>Protection</b> = artificial advantage given to domestic industries; tariff/quota removal forces cost-cutting to compete.</li><li>Broad and <b>indirect</b> — vs legal regulation which is specific and compulsory.</li><li>Process link: changes the cost of <b>inputs</b> (fuel taxes, subsidies), rules of <b>transformation</b> (WHS, employment relations), demand for <b>outputs</b> (travel restrictions).</li></ul>',
  '<ul><li>Government <b>blocked Qatar Airways\' extra flights (2023–24)</b> — de facto protection.</li><li>Domestic aviation fuel taxed <b>6c/L</b>; <b>Sydney Airport Curfew Act 1995</b> (11pm–6am, $550k fines) shapes scheduling.</li><li>Net-zero-2050 policy → Qantas secured <b>500M litres SAF p.a. from 2028</b>.</li><li>~<b>$2.7bn</b> COVID assistance (incl. ~$900M JobKeeper) kept operations alive.</li></ul>'),
 'Operations influences (umbrella)': (
  '"Influences on operations refers to the <b>various internal and external factors that impact the way a business manages and conducts its operational processes</b>."',
  '<ul><li>The seven + CSR: <b>G</b>lobalisation, <b>T</b>echnology, <b>G</b>overnment policies, <b>L</b>egal regulation, <b>E</b>nvironmental sustainability, <b>Co</b>st-based competition, <b>Q</b>uality expectations + <b>CSR</b> ("GTG LECoQ + CSR").</li><li>External factors present <b>both threat and opportunity</b> — the business must adjust.</li><li>Each influence should be paired with a strategy that "makes sense" (e.g. quality expectations → quality management).</li></ul>',
  '<ul><li>One example each: globalisation (Oneworld 900 destinations) · technology (RFID −30% mishandled bags) · quality expectations (NPS +24 FY24) · cost-based competition (Jetstar 11M sub-$100 fares) · government (Qatar block) · legal (ACCC $100M penalty) · environment (net zero 2050) · CSR (45,000 free flights after Rex/Bonza).</li></ul>'),
 'Transformed resources': (
  '"The inputs which are <b>changed or converted into something else, or acted upon</b> by the operation to produce goods or services."<br><br>The three: <b>M</b>aterials, <b>I</b>nformation, <b>C</b>ustomers.',
  '<ul><li><b>Materials</b>: basic elements of production — raw materials (unprocessed) + intermediate goods (already manufactured) = "direct materials".</li><li><b>Information</b>: knowledge from research/investigation/instruction — external (ABS) and internal (reports, feedback, KPIs); guides how other inputs are used.</li><li><b>Customers</b>: their needs "<b>drive</b>" operations, their choices shape inputs/processes — and they are themselves transformed (physically, emotionally, psychologically).</li></ul>',
  '<ul><li><b>Materials</b>: aviation fuel (~3.5 billion litres a year), in-flight meals.</li><li><b>Information</b>: ECAM aircraft-monitoring memos + ACARS performance data on every flight; booking data.</li><li><b>Customers</b>: <b>51.8M passengers FY24</b> literally transformed from city A to city B; 16.4M frequent flyers as repeat transformed customers.</li></ul>'),
 'Transforming resources': (
  '"The inputs that <b>carry out the transformation process</b> — used to transform other resources but not themselves part of the finished product."<br><br>The two: <b>H</b>uman <b>R</b>esources + <b>F</b>acilities.',
  '<ul><li><b>Human resources</b>: employees providing the <b>skills, knowledge, capabilities and labour</b> to convert materials into goods/services — "the most important asset"; well-trained, communicative HR is crucial.</li><li><b>Facilities</b>: the <b>plant and machinery</b> used in operations — key decisions on location, design/process layout, number of facilities, capacity.</li></ul>',
  '<ul><li><b>HR</b>: 27,000+ staff (93% Australia-based) — pilots, cabin crew, engineers, ground crew; growing to ~32,000 by 2033.</li><li><b>Facilities</b>: <b>347-aircraft fleet</b>, terminals, maintenance hangars (Brisbane/Sydney/LA), and the <b>$20M Sydney simulator training centre</b> (opened 2024, trains 4,500 pilots/crew a year).</li></ul>'),
 'Outputs': (
  '"Outputs are the <b>finished goods or services</b> produced by the operations function that have a <b>value to customers greater than the cost of inputs</b>." Profit requires output revenue &gt; input expenditure.',
  '<ul><li>Two subtler outputs: <b>customer service</b> ("how well a business meets and exceeds customer expectations" — one dissatisfied customer tells ~11 others) and <b>warranties</b> ("promises to correct any defects").</li><li>The feedback loop: <b>warranty-claim numbers signal issues inside the operations process</b> → feeds monitoring, control and improvement.</li><li>Competition and Consumer Act 2010: outputs must match description, be fit for purpose, defect-free.</li></ul>',
  '<ul><li>Service guarantees instead of typical warranties: refunds/compensation for cancellations, <b>$50–100/day baggage-delay compensation, up to $2,000 for lost bags</b>.</li><li>NPS as the output KPI: domestic NPS <b>+24 points FY24</b>; Closed Loop Feedback program.</li><li>Qantas Freight revenue $1.2B FY24, <b>+11% in 1H FY25</b>.</li></ul>'),
 'Operations strategies (umbrella)': (
  '"The strategies that operations managers may use to <b>achieve operations goals and broader business goals</b>… An effective operations strategy will give a business a <b>competitive advantage</b>."',
  '<ul><li>The nine ("POGO SQuINT"): <b>P</b>erformance objectives, <b>O</b>utsourcing, <b>G</b>lobal factors, <b>O</b>vercoming resistance to change, <b>S</b>CM, <b>Qu</b>ality management, <b>I</b>nventory management, <b>N</b>ew product/service design &amp; development, <b>T</b>echnology.</li><li>All strategies relate to producing the good/service — each one should be linked to the process stage it improves (inputs, transformation, outputs).</li></ul>',
  '<ul><li>One example each: technology ($12bn fleet renewal) · outsourcing (1,700 ground handlers, ~$100M/yr) · inventory (JIT fuel + spare parts) · quality management (Kaizen 2024, A-checks) · new product (Project Sunrise, mid-2026) · global factors (60% domestic share H1 FY25 = economies of scale) · overcoming resistance ($1bn redundancies, $275M/yr training).</li></ul>'),
 'Performance objectives': (
  '"Performance objectives are <b>goals that relate to particular aspects of the transformation processes</b>" — quantifiable targets/KPIs that gauge and guide operational efficiency.',
  '<ul><li><b>Quality</b> — being right (design / conformance / service)</li><li><b>Speed</b> — being fast (wait times, lead times)</li><li><b>Dependability</b> — being on time (warranty claims / complaints)</li><li><b>Flexibility</b> — being able to change</li><li><b>Customisation</b> — more options (mass customisation)</li><li><b>Cost</b> — being productive (minimise expenses)</li></ul>Mnemonic: "QueSaDela Football CClub".',
  '<ul><li>Quality: <b>$12bn fleet renewal</b> from 2024.</li><li>Speed: Project Sunrise cuts travel ~<b>4 hours</b>; 35-min turnarounds.</li><li>Dependability: OTP <b>80%</b> + cancellations <b>2.5%</b> (2024) vs 44%/6.7% (2022).</li><li>Flexibility: <b>28 A321XLRs in 2025 (FY25)</b>; COVID freight pivot ($1.32bn FY21).</li><li>Customisation: Classic Plus — 20M reward seats, +13% redemptions.</li><li>Cost: <b>9.73c/ASK FY24, −4.5%</b>.</li></ul>'),
 'New product or service design and development': (
  '"Creating and introducing new offerings to meet market demands or technological advancements — <b>researching customer needs, designing a product to fulfil those needs, testing it and then implementing it</b>."',
  '<ul><li><b>Consumer approach</b> (market research decides features/quality) vs <b>capability approach</b> (new technology enables advanced functionality).</li><li>Service design: <b>explicit service</b> (tangible — time, expertise, skill) vs <b>implicit service</b> (intangible feeling of being looked after); more standardisation = lower operating costs.</li><li>Design considerations = the process link: <b>supply chain, quality, capacity, cost</b>.</li></ul>',
  '<ul><li><b>Project Sunrise</b>: 12 A350-1000s, 19-hour non-stop Sydney–London/NY, launching <b>mid-2026</b>, peak spend <b>$1.2bn into FY25–26</b>; wellness zones, redesigned cabins.</li><li>A220 cabins (largest single-aisle windows, fast free Wi-Fi); 8 new 787-9 Dreamliners (20% less fuel); Perth–Paris route.</li><li><b>Classic Plus</b> rewards launched FY24 — $120M, 20M+ reward seats, redemptions +13%.</li></ul>'),
 'Logistics': (
  '"The part of the supply chain that focuses on <b>moving inputs, resources and outputs through the supply chain as quickly as possible</b>, saving as much time at each point as possible."',
  '<ul><li>Components: <b>transportation</b>, <b>storage</b> (secure holding of stock), <b>warehousing</b> (storage, protection, later distribution), <b>distribution centres</b> (short-term only), <b>materials handling</b> (loading/unloading — pallets, forklifts, containers), packaging.</li><li>Goal: "an <b>efficient steady flow</b> of material through the supply chain."</li></ul>',
  '<ul><li>Direct oil pipeline <b>Kurnell refinery → Sydney Airport</b> with 750M litres of storage.</li><li><b>22,500 sqm Mascot distribution centre</b>; JETS Transport Express.</li><li>Coordinates the physical inputs behind every flight: catering, baggage, fuel, crew positioning — which let Qantas absorb the <b>132% flying rebound</b> FY23 vs FY22.</li></ul>'),
 'E-commerce and global sourcing': (
  '<b>E-commerce</b>: "the <b>buying of inputs via the internet</b>" (SCM context).<br><b>Global sourcing</b>: "businesses <b>purchasing supplies or services without being constrained by location</b>" — buying wherever best meets requirements.',
  '<ul><li>E-commerce <b>B2B</b>: e-procurement auto-reorders when stock runs low → prevents supply shortfalls. <b>B2C</b>: selling online removes intermediaries/wholesalers → cheaper prices.</li><li>Global sourcing upside: cheapest/best-quality inputs worldwide; downside: <b>exchange rates, differing laws, longer lead times</b>.</li></ul>',
  '<ul><li>E-commerce: <b>97% of sales online</b>; ~70% of bookings via qantas.com/app; 8.5M monthly website visits; TripADeal +60%.</li><li>Global sourcing: aircraft from <b>Airbus/Boeing bought in USD</b>; SAF from London (BP) and <b>California (20M L p.a. from 2025 — FY25)</b>; offshore maintenance providers.</li></ul>'),
 'Quality management: control, assurance and improvement': (
  '"Quality management refers to the <b>maintenance of consistency, reliability and sustainability</b> to ensure the product <b>meets the quality expectations of the customer</b>." Three components: control, assurance, improvement.',
  '<ul><li><b>Quality control (detection)</b>: monitoring + corrective action — <b>feed-forward</b> (before production = inputs), <b>concurrent</b> (during = transformation), <b>feedback</b> (final product = outputs).</li><li><b>Quality assurance (prevention)</b>: quality assured <b>before reaching the market</b> — proactive; ISO 9001 certification.</li><li><b>Quality improvement (continuous)</b>: continuous improvement + <b>TQM</b> (benchmarking, employee empowerment, customer focus, continuous improvement); Kaizen, Six Sigma.</li><li>Rugby: QA = game prep, QC = in-game adjustments, QI = reviewing the tape.</li></ul>',
  '<ul><li>Control: <b>A-checks every 400–600 flight hours</b> (200–300 flights); 2019 737 wing-crack inspections (33 checked, 2 grounded).</li><li>Assurance: <b>IOSA registration + CASA benchmarks</b> (200+ audits); ISO 9001.</li><li>Improvement: <b>Kaizen adopted 2024</b>; Lean Six Sigma; Skytrax recovered <b>24th → 14th (2025)</b>; cancellations 7.1% → 2.5% in 2022.</li></ul>'),
 'Global factors': (
  '"Global factors refer to the <b>strategies a business can use in a global environment to improve the operations process</b>."<br><br>The four: global sourcing, economies of scale, scanning and learning, research and development.',
  '<ul><li><b>Global sourcing</b>: acquire inputs worldwide to cut costs / lift quality.</li><li><b>Economies of scale</b>: unit costs fall as production scales.</li><li><b>Scanning and learning</b>: watch global trends, implement them at home.</li><li><b>R&amp;D</b>: systematic work to improve products and processes.</li><li>Quotable link: "<b>R&amp;D improves processes; scanning and learning improves strategies.</b>"</li></ul>',
  '<ul><li>Scale: <b>60% of domestic passengers H1 FY25</b>; flying hours +25% while unit costs −5.2%.</li><li>Scanning: Emirates alliance; <b>Jetstar Asia</b> in a region forecast for 50% aviation growth.</li><li>R&amp;D: <b>$50M mustard-seed SAF research</b>; Constellation flight planning (with the Australian Centre for Field Robotics); Project Sunrise.</li><li>Sourcing: Airbus/Boeing aircraft; SAF from London/California.</li></ul>'),
 'Economies of scale': (
  '"The <b>cost advantages a business obtains due to their scale of operation</b> — as production increases, <b>cost per unit falls</b>, meaning profitability will rise."',
  '<ul><li>Why: <b>fixed costs</b> (rent, machinery, aircraft, training infrastructure) are <b>spread over more units</b> + <b>bulk-buying discounts</b>.</li><li>Selling into the global market increases scale further.</li><li>Lower unit cost → cheaper COGS → higher gross profit → more competitive pricing.</li><li>Limit: only up to the technical optimum — beyond it, costs rise again.</li></ul>',
  '<ul><li>Group carried <b>60% of domestic passengers in H1 FY25 (FY25)</b>.</li><li>Total flying hours <b>+25%</b> (2023→24) while unit costs fell <b>5.2%</b>.</li><li>Fixed costs — the <b>$525M Sydney terminal lease</b>, hangars, training centres — spread across ~<b>820 daily flights</b>.</li><li>~$12bn procurement scale → better supplier deals.</li></ul>'),
 'Scanning and learning': (
  '"The <b>systematic process of acquiring information about changes and trends in external economic conditions</b> and using them to make decisions about operations. <b>Scanning</b> is looking overseas to find new business ideas and trends; <b>learning</b> is the implementation of this information by changing processes domestically."',
  '<ul><li>Constant watch on <b>global trends, technological advancements and market shifts</b> → adjust strategies and operations proactively.</li><li>Builds a culture of <b>continuous improvement and adaptability</b>, sustaining long-term growth.</li><li>Pairs naturally with benchmarking against world-leading competitors.</li></ul>',
  '<ul><li><b>Emirates alliance</b> — leveraging Emirates\' Dubai hub and infrastructure learnings.</li><li><b>Jetstar Asia</b> expansion into a region with 50% forecast aviation growth over 10 years.</li><li>NPS <b>benchmarked against Emirates</b>; watched global fleet trends → adopted fuel-efficient A321XLR/787 and cabin tech (Wi-Fi, IFE).</li></ul>'),
}

for term, (definition, build, qantas) in TERMS.items():
    DECK.add_note(genanki.Note(model=MODEL, fields=[DEF + f'Define: <b>{term}</b>', definition]))
    DECK.add_note(genanki.Note(model=MODEL, fields=[BLD + f'Build on: <b>{term}</b>', build]))
    DECK.add_note(genanki.Note(model=MODEL, fields=[QAN + f'Qantas evidence for: <b>{term}</b>', qantas]))

genanki.Package([DECK]).write_to_file('Operations-ER-Paragraph-Drills.apkg')
print(f'Wrote Operations-ER-Paragraph-Drills.apkg with {len(TERMS) * 3} cards ({len(TERMS)} terms x 3)')
