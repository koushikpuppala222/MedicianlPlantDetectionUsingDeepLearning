from flask import *
import os
from werkzeug.utils import secure_filename
import label_image

def load_image(image):
    text = label_image.main(image)
    return text

app = Flask(__name__)

@app.route('/')
@app.route('/first')
def first():
    return render_template('first.html')

 
  
    
@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/chart')
def chart():
    return render_template('chart.html')


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']
        file_path = secure_filename(f.filename)
        f.save(file_path)
        # Make prediction
        result = load_image(file_path)
        result = result.title()
        d = {"Asthma Plant":" → Euphorbia hirta is a pantropical weed, originating from the tropical regions of the Americas. It is a hairy herb that grows in open grasslands, roadsides and pathways. It is widely used in traditional herbal medicine across many cultures, particularly for asthma, skin ailments, and hypertension.",
	'Avaram':" → Senna auriculata is a leguminous tree in the subfamily Caesalpinioideae. It is commonly known by its local names matura tea tree, avaram or ranawara, or the English version avaram senna. It is the State flower of Telangana. It occurs in the dry regions of India and Sri Lanka. ",
        "Balloon Vine":" → Cardiospermum halicacabum, known as the lesser balloon vine, balloon plant or love in a puff, is a climbing plant widely distributed across tropical and subtropical areas of Africa, Australia, and North America that is often found as a weed along roads and rivers.",
        "Bellyache Bush":" → Jatropha gossypiifolia, commonly known as bellyache bush, black physicnut or cotton-leaf physicnut, is a species of flowering plant in the spurge family, Euphorbiaceae. The species is native to Mexico, Philippines, South America, Gujarat State, and the Caribbean islands. ",
        "Benghal Dayflower":" → Commelina benghalensis, commonly known as the Benghal dayflower, tropical spiderwort, or wandering Jew, kanshira in Bengali, is a perennial herb native to tropical Asia and Africa",
        "Big Caltrops":" → A caltrop also known as caltrap, galtrop, cheval trap, galthrap, galtrap, calthrop, jackrock or crow's foot is an area denial weapon made up of two or more sharp nails or spines arranged in such a manner that one of them always points upward from a stable base for example, a tetrahedron. Historically, caltrops were part of defences that served to slow the advance of troops, especially horses, chariots, and war elephants, and were particularly effective against the soft feet of camels. In modern times, caltrops are effective when used against wheeled vehicles with pneumatic tires.",
        "Black Honey Shrub":" → Black-Honey Shrub is usually a much-branched somewhat climbing shrub, rarely a small tree. Leaves are ovate-oblong to elliptic, 1-5 cm long, 0.7-3 cm wide, produced on short lateral branchlets, looking like leaflets of a compound leaf.",
        "Bristly Wild Grape":" → Cyphostemma setosum - Bristly Wild Grape. Bristly Wild Grape is a succulent climber clothed with bristly hairs. Leaves are trifoliate rarely lower ones simple, fleshy, nearly stalkless, shortly stalked, elliptic, ovoate to obovate, blunt, rounded at the base, stringly sawtoothed, up to 7 x 5 cms.31-Dec-2016",
        "Butterfly Pea":" → Clitoria ternatea, commonly known as Asian pigeonwings, bluebellvine, blue pea, butterfly pea, cordofan pea or Darwin pea is a plant species belonging to the family Fabaceae, endemic and native to the Indonesian island of Ternate. In India, it is revered as a holy flower, used in daily puja rituals.",
        'Cape Gooseberry':" → Physalis peruviana, is a South American plant native to Colombia, Ecuador and Peru in the nightshade family, commonly known as Cape gooseberry or goldenberry, known in its countries of origin as ",
        "Common Wireweed":" → Sida acuta, the common wireweed, is a species of flowering plant in the mallow family, Malvaceae. It is believed to have originated in Central America, but today has a pantropical distribution and is considered a weed in some areas.",
        "Country Mallow":" → Sida cordifolia is a perennial subshrub of the mallow family Malvaceae native to India. It has naturalized throughout the world, and is considered an invasive weed in Africa, Australia, the southern United States, Hawaiian Islands, New Guinea, and French Polynesia.",
        "Crown Flower":" → Calotropis gigantea, the crown flower, is a species of Calotropis native to Cambodia, Vietnam, Bangladesh, Indonesia, Malaysia, Thailand, Sri Lanka, India, China, Pakistan, and Nepal. It is a large shrub growing to 4 m tall. It has clusters of waxy flowers that are either white or lavender in colour.",
        "Green Chireta":" → Andrographis paniculata, commonly known as creat or green chiretta, is an annual herbaceous plant in the family Acanthaceae, native to India and Sri Lanka. It is widely cultivated in Southern and Southeastern Asia, where it has been believed to be a treatment for bacterial infections and some diseases.",
        "Holy Basil":" → Ocimum tenuiflorum, commonly known as holy basil, tulsi or tulasi, is an aromatic perennial plant in the family Lamiaceae. It is native to the Indian subcontinent and widespread as a cultivated plant throughout the Southeast Asian tropics",
        "Indian Copperleaf":" → Acalypha indica is an herbaceous annual that has catkin-like inflorescences with cup-shaped involucres surrounding the minute flowers. It is mainly known for its root being attractive to domestic cats, and for its various medicinal uses. It occurs throughout the Tropics. ",
        "Indian Jujube":" → Ziziphus mauritiana, also known as Indian jujube, Indian plum, Chinese date, Chinese apple, ber, and dunks is a tropical fruit tree species belonging to the family Rhamnaceae. ",
	'Indian Sarsaparilla':" → Hemidesmus indicus, Indian sarsaparilla is a species of plant found in South Asia. It occurs over the greater part of India, from the upper Gangetic plain eastwards to Assam and in some places in central, western and South India. The root is a substitute for sarsaparilla.",
        "Indian Stinging Nettle":" → Tragia involucrata, the Indian stinging nettle, is a species of plant in the family Euphorbiaceae.",
        "Indian Thornapple":" → Datura innoxia, known as pricklyburr, recurved thorn-apple, downy thorn-apple, Indian-apple, lovache, moonflower, nacazcul, toloatzin, toloaxihuitl, tolguache or toloache, is a species of flowering plant in the family Solanaceae. ",
        "Indian Wormwood":" → Indian Wormwood is found in India and East Asia. It is found in the Himalayas at altitudes of 300-2400 m. Flowering: August-October. Medicinal uses: An infusion of leaves is used in the treatment of nervous and spasmodic affections, in asthma and in diseases of the brain.",
        "Ivy Gourd":" → Ivy gourd is a plant. The leaves, root, and fruit are used to make medicine. Ivy gourd is most often used for diabetes. People also use ivy gourd for gonorrhea, constipation, wounds, and other conditions, but there is no good scientific evidence to support these uses.",
        "Kokilaksha":" → The plant is an Ayurvedic herb used to make medicines for several gastrointestinal, kidney, reproductive, liver, and bone disorders. Kokilaksha is native to India and also to other places like Srilanka, Malaysia, Nepal and Myanmar. Kokilaksha means having eyes like Kokila the Indian cuckoo.",
        "Land Caltrops":" → Tribulus terrestris is an annual plant in the caltrop family widely distributed around the world. It is adapted to thrive in dry climate locations in which few other plants can survive. It is native to warm temperate and tropical regions in southern Eurasia and Africa. ",
        "Madagascar Periwinkle":" → Catharanthus roseus, commonly known as bright eyes, Cape periwinkle, graveyard plant, Madagascar periwinkle, old maid, pink periwinkle, rose periwinkle, is a species of flowering plant in the family Apocynaceae. It is native and endemic to Madagascar, but grown elsewhere as an ornamental and medicinal plant. ",
        'Madras Pea Pumpkin':" → Madras pea pumpkin is a perennial herb, climbing or trailing up to 3 m, stem bristly-hairy. Tendrils are simple, thread-like. Leaves are arrow shaped, hastate, ...",
        "Malabar Catmint":" → Anisomeles indica, or catmint, is a species of herbaceous plant native to eastern Asia and naturalized on some Pacific islands.",
        "Mexican Mint":" → Coleus amboinicus, synonym Plectranthus amboinicus, is a semi-succulent perennial plant in the family Lamiaceae with a pungent oregano-like flavor and odor",
        "Mexican Prickly Poppy":" → Argemone mexicana is a species of poppy found in Mexico and now widely naturalized in many parts of the world. An extremely hardy pioneer plant, it is tolerant of drought and poor soil, often being the only cover on new road cuttings or verges. It has bright yellow latex. ",
        "Mountain Knotgrass":" → Aerva lanata, the mountain knotgrass, is a woody, prostrate or succulent, perennial herb in the family Amaranthaceae, native to Asia, Africa. It has been included as occurring in Australia by the US government, but it is not recognised as occurring in Australia by any Australian state herbarium.",
        "Nalta Jute":" → Jute mallow or nalta jute is a species of shrub in the family Malvaceae. Together with C. capsularis it is the primary source of jute fiber. The leaves and young fruits are used as a vegetable, the dried leaves are used for tea and as a soup thickener, and the seeds are edible.",
        "Night Blooming Cereus":" → Regardless of genus or species, night-blooming cereus flowers are almost always white or very pale shades of other colors, often large, and frequently fragrant. Most of the flowers open after nightfall, and by dawn, most are in the process of wilting.",
        "Panicled Foldwing":" → Dicliptera paniculata - Panicled Foldwing. Panicled Foldwing is an erect herb, 0.6-1.2 m tall. Young shoots are usually 4-sided; adult shoots 6-sided, white spreading bristle-hairy. Ovate leaves opposite, equal and unequal; leaf-stalk 3-5 mm.",
        "Prickly Chaff Flower":" → Achyranthes aspera is a species of plant in the family Amaranthaceae. It is distributed throughout the tropical world. It can be found in many places growing as an introduced species and a common weed. It is an invasive species in some areas, including many Pacific Islands environments.",
        "Punarnava":" → Boerhaavia diffusa is a species of flowering plant in the four o'clock family which is commonly known as punarnava, red spiderling, spreading hogweed, or tarvine. It is taken in herbal medicine for pain relief and other uses. The leaves of Boerhaavia diffusa are often used as a green vegetable in many parts of India.",
        'Purple Fruited Pea Eggplant':" → It is a very good brain stimulant. It removes chest, nose and head congestion. It relieves cough and cold. It relieves dyspepsia impairment of digestion",
        "Purple Tephrosia":" → Tephrosia purpurea is a species of flowering plant in the family Fabaceae, that has a pantropical distribution. It is a common wasteland weed. In many parts it is under cultivation as green manure crop. It is found throughout India and Sri Lanka in poor soils. Common names include: Bengali",
        "Rosary Pea":" → Abrus precatorius, commonly known as jequirity bean or rosary pea, is a herbaceous flowering plant in the bean family Fabaceae. It is a slender, perennial climber with long, pinnate-leafleted leaves that twines around trees, shrubs, and hedges. ",
        "Shaggy Button Weed":" → Landrina, Spermacoce hispida, SHAGGY BUTTON WEED - Herbal Medicine - An illustrated compilation of Philippine medicinal plants by Dr Godofredo Umali Stuart .",
        "Small Water Clover":" →  Water clovers are fast growers, with vestita and quadrifolia ranging between 4 inches and one foot of maximum height, depending on water depth ...",
        "Spiderwisp":" → It is known by many common names including Shona cabbage, African cabbage, spiderwisp, cat's whiskers, chinsaga and stinkweed. It is an annual wildflower native to Africa but has become widespread in many tropical and sub-tropical parts of the world.",
        "Square Stalked Vine":" → This site makes an attempt to gather and share common names of the plants found in India. The common names are just as important as the scientific names.",
        "Stinking Passionflower":" → Native to South America, stinking passionflower is a climbing vine with an unpleasant smell and flowers that resemble those of the passionfruit vine. Stinking passionflower can invade forest edges, coastal vegetation, roadsides and disturbed areas. It is widespread in northern Queensland.",
        "Sweet Basil":" → Basil, also called great basil, is a culinary herb of the family Lamiaceae. It is a tender plant, and is used in cuisines worldwide. In Western cuisine, the generic term basil refers to the variety also known as sweet basil or Genovese basil. Basil is native to tropical regions from Central Africa to Southeast Asia.",
        "Sweet Flag":" → Acorus calamus is a species of flowering plant with psychoactive chemicals. It is a tall wetland monocot of the family Acoraceae, in the genus Acorus",
        "Tinnevelly Senna":" → Senna alexandrina is an ornamental plant in the genus Senna. It is used in herbalism. It grows natively in upper Egypt, especially in the Nubian region, and near Khartoum, where it is cultivated commercially. It is also grown elsewhere, notably in India and Somalia. ",
        'Trellis Vine':" → Unlike a tree, vines can't support themselves, so a trellis provides this support. Also, trellises keep vines off the ground and therefore minimize disease. They help spread out the canopy for sun exposure, pruning and canopy management.",
        "Velvet Bean":" → Mucuna pruriens is a tropical legume native to Africa and tropical Asia and widely naturalized and cultivated. Its English common names include monkey tamarind, velvet bean, Bengal velvet bean, Florida velvet bean, Mauritius velvet bean, Yokohama velvet bean, cowage, cowitch, lacuna bean, and Lyon bean. ",
        "Aloevara":" → Aloe vera is a succulent plant species of the genus Aloe. It is widely distributed, and is considered an invasive species in many world regions. An evergreen perennial, it originates from the Arabian Peninsula, but grows wild in tropical, semi-tropical, and arid climates around the world",
        "Coatbuttons":" → Tridax procumbens, commonly known as coatbuttons or tridax daisy, is a species of flowering plant in the family Asteraceae. It is best known as a widespread weed and pest plant.",
        "Heart Leaved Moonseed":" → Tinospora cordifolia is a herbaceous vine of the family Menispermaceae indigenous to tropical regions of the Indian subcontinent. It has been used in Ayurveda to treat various disorders, but there is no clinical evidence for the effectiveness of such treatment.",
        "Nagfani":" → Crataegus, commonly called hawthorn, quickthorn, thornapple, May-tree, whitethorn, Mayflower, or hawberry, is a genus of several hundred species of shrubs and trees in the family Rosaceae, native to temperate regions of the Northern Hemisphere in Europe, Asia, North Africa, and North America.",
        "Neem":" → Azadirachta indica, commonly known as neem, nimtree or Indian lilac, is a tree in the mahogany family Meliaceae. It is one of two species in the genus Azadirachta, and is native to the Indian subcontinent. It is typically grown in tropical and semi-tropical regions. Neem trees also grow on islands in southern Iran.", 
        "Tulsi":" → Tulsi has also been shown to counter metabolic stress through normalization of blood glucose, blood pressure and lipid levels, and psychological stress through positive effects on memory and cognitive function and through its anxiolytic and anti-depressant properties.",
        "Zzz":"-> Good for health ."}
       
        result = result+d[result]
        #result2 = result+d[result]
        #result = [result]
        #result3 = d[result]        
        print(result)
        #print(result3)
        os.remove(file_path)
        return result
        #return result3
    return None

if __name__ == '__main__':
    app.run()