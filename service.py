# -*- coding: utf-8 -*-
from aligned_treemap import treemap as tp
import json
import numpy as np


# Color map
# matplotlib.cm.get_cmap('GnBu')
c = [
    (0.9686274509803922, 0.9882352941176471, 0.9411764705882353, 1.0),
    (0.9657977700884275, 0.987128027681661, 0.9385928489042675, 1.0),
    (0.9629680891964629, 0.9860207612456747, 0.9360092272202999, 1.0),
    (0.9601384083044983, 0.9849134948096886, 0.9334256055363321, 1.0),
    (0.9573087274125336, 0.9838062283737025, 0.9308419838523645, 1.0),
    (0.954479046520569, 0.9826989619377163, 0.9282583621683967, 1.0),
    (0.9516493656286044, 0.9815916955017301, 0.925674740484429, 1.0),
    (0.9488196847366398, 0.980484429065744, 0.9230911188004614, 1.0),
    (0.9459900038446751, 0.9793771626297578, 0.9205074971164936, 1.0),
    (0.9431603229527105, 0.9782698961937717, 0.917923875432526, 1.0),
    (0.9403306420607459, 0.9771626297577855, 0.9153402537485582, 1.0),
    (0.9375009611687812, 0.9760553633217993, 0.9127566320645906, 1.0),
    (0.9346712802768166, 0.9749480968858132, 0.9101730103806228, 1.0),
    (0.931841599384852, 0.9738408304498269, 0.9075893886966551, 1.0),
    (0.9290119184928873, 0.9727335640138408, 0.9050057670126874, 1.0),
    (0.9261822376009228, 0.9716262975778547, 0.9024221453287197, 1.0),
    (0.9233525567089581, 0.9705190311418685, 0.899838523644752, 1.0),
    (0.9205228758169934, 0.9694117647058823, 0.8972549019607843, 1.0),
    (0.9176931949250289, 0.9683044982698962, 0.8946712802768165, 1.0),
    (0.9148635140330642, 0.96719723183391, 0.8920876585928489, 1.0),
    (0.9120338331410995, 0.9660899653979238, 0.8895040369088811, 1.0),
    (0.909204152249135, 0.9649826989619377, 0.8869204152249135, 1.0),
    (0.9063744713571703, 0.9638754325259515, 0.8843367935409457, 1.0),
    (0.9035447904652056, 0.9627681660899654, 0.881753171856978, 1.0),
    (0.9007151095732411, 0.9616608996539792, 0.8791695501730104, 1.0),
    (0.8978854286812764, 0.960553633217993, 0.8765859284890426, 1.0),
    (0.8950557477893117, 0.9594463667820069, 0.874002306805075, 1.0),
    (0.8922260668973472, 0.9583391003460208, 0.8714186851211072, 1.0),
    (0.8893963860053825, 0.9572318339100345, 0.8688350634371396, 1.0),
    (0.886566705113418, 0.9561245674740484, 0.8662514417531718, 1.0),
    (0.8837370242214533, 0.9550173010380623, 0.8636678200692041, 1.0),
    (0.8809073433294886, 0.9539100346020761, 0.8610841983852364, 1.0),
    (0.8781237985390234, 0.9528181468665897, 0.8584851980007688, 1.0),
    (0.8756632064590543, 0.951833910034602, 0.8557785467128027, 1.0),
    (0.873202614379085, 0.9508496732026144, 0.8530718954248365, 1.0),
    (0.8707420222991157, 0.9498654363706266, 0.8503652441368704, 1.0),
    (0.8682814302191465, 0.9488811995386389, 0.8476585928489042, 1.0),
    (0.8658208381391772, 0.9478969627066512, 0.8449519415609381, 1.0),
    (0.863360246059208, 0.9469127258746636, 0.8422452902729719, 1.0),
    (0.8608996539792387, 0.9459284890426758, 0.8395386389850057, 1.0),
    (0.8584390618992696, 0.9449442522106881, 0.8368319876970396, 1.0),
    (0.8559784698193003, 0.9439600153787004, 0.8341253364090734, 1.0),
    (0.8535178777393311, 0.9429757785467128, 0.8314186851211073, 1.0),
    (0.8510572856593618, 0.9419915417147251, 0.8287120338331411, 1.0),
    (0.8485966935793926, 0.9410073048827373, 0.826005382545175, 1.0),
    (0.8461361014994233, 0.9400230680507496, 0.8232987312572088, 1.0),
    (0.8436755094194541, 0.939038831218762, 0.8205920799692425, 1.0),
    (0.8412149173394848, 0.9380545943867743, 0.8178854286812764, 1.0),
    (0.8387543252595155, 0.9370703575547865, 0.8151787773933102, 1.0),
    (0.8362937331795464, 0.9360861207227988, 0.8124721261053441, 1.0),
    (0.8338331410995771, 0.9351018838908112, 0.8097654748173779, 1.0),
    (0.8313725490196079, 0.9341176470588235, 0.8070588235294117, 1.0),
    (0.8289119569396386, 0.9331334102268358, 0.8043521722414456, 1.0),
    (0.8264513648596694, 0.932149173394848, 0.8016455209534794, 1.0),
    (0.8239907727797001, 0.9311649365628604, 0.7989388696655133, 1.0),
    (0.8215301806997309, 0.9301806997308727, 0.7962322183775471, 1.0),
    (0.8190695886197616, 0.929196462898885, 0.7935255670895809, 1.0),
    (0.8166089965397925, 0.9282122260668974, 0.7908189158016148, 1.0),
    (0.8141484044598232, 0.9272279892349096, 0.7881122645136486, 1.0),
    (0.8116878123798539, 0.9262437524029219, 0.7854056132256825, 1.0),
    (0.8092272202998847, 0.9252595155709342, 0.7826989619377163, 1.0),
    (0.8067666282199155, 0.9242752787389465, 0.7799923106497502, 1.0),
    (0.8043060361399462, 0.9232910419069588, 0.777285659361784, 1.0),
    (0.8018454440599769, 0.9223068050749711, 0.7745790080738177, 1.0),
    (0.7988927335640139, 0.9211380238369857, 0.7720569011918493, 1.0),
    (0.7944636678200693, 0.9194156093810073, 0.7700884275278739, 1.0),
    (0.7900346020761246, 0.9176931949250288, 0.7681199538638985, 1.0),
    (0.78560553633218, 0.9159707804690503, 0.7661514801999232, 1.0),
    (0.7811764705882354, 0.9142483660130718, 0.7641830065359477, 1.0),
    (0.7767474048442907, 0.9125259515570934, 0.7622145328719724, 1.0),
    (0.7723183391003461, 0.910803537101115, 0.7602460592079969, 1.0),
    (0.7678892733564014, 0.9090811226451364, 0.7582775855440216, 1.0),
    (0.7634602076124568, 0.907358708189158, 0.7563091118800461, 1.0),
    (0.7590311418685122, 0.9056362937331796, 0.7543406382160708, 1.0),
    (0.7546020761245675, 0.903913879277201, 0.7523721645520954, 1.0),
    (0.7501730103806229, 0.9021914648212226, 0.75040369088812, 1.0),
    (0.7457439446366783, 0.9004690503652442, 0.7484352172241446, 1.0),
    (0.7413148788927336, 0.8987466359092656, 0.7464667435601692, 1.0),
    (0.736885813148789, 0.8970242214532872, 0.7444982698961938, 1.0),
    (0.7324567474048443, 0.8953018069973087, 0.7425297962322184, 1.0),
    (0.7280276816608997, 0.8935793925413302, 0.740561322568243, 1.0),
    (0.7235986159169551, 0.8918569780853518, 0.7385928489042676, 1.0),
    (0.7191695501730104, 0.8901345636293734, 0.7366243752402922, 1.0),
    (0.7147404844290658, 0.8884121491733948, 0.7346559015763169, 1.0),
    (0.7103114186851212, 0.8866897347174164, 0.7326874279123414, 1.0),
    (0.7058823529411765, 0.8849673202614379, 0.7307189542483661, 1.0),
    (0.7014532871972319, 0.8832449058054594, 0.7287504805843906, 1.0),
    (0.6970242214532872, 0.881522491349481, 0.7267820069204153, 1.0),
    (0.6925951557093426, 0.8798000768935025, 0.7248135332564398, 1.0),
    (0.688166089965398, 0.878077662437524, 0.7228450595924645, 1.0),
    (0.6837370242214533, 0.8763552479815456, 0.7208765859284891, 1.0),
    (0.6793079584775087, 0.8746328335255671, 0.7189081122645137, 1.0),
    (0.674878892733564, 0.8729104190695887, 0.7169396386005383, 1.0),
    (0.6704498269896194, 0.8711880046136101, 0.7149711649365629, 1.0),
    (0.6660207612456748, 0.8694655901576317, 0.7130026912725875, 1.0),
    (0.6615916955017301, 0.8677431757016533, 0.7110342176086121, 1.0),
    (0.6567474048442906, 0.8658823529411765, 0.7104959630911188, 1.0),
    (0.6512110726643598, 0.8637908496732026, 0.7123414071510957, 1.0),
    (0.6456747404844292, 0.8616993464052288, 0.7141868512110727, 1.0),
    (0.6401384083044983, 0.8596078431372549, 0.7160322952710496, 1.0),
    (0.6346020761245674, 0.8575163398692811, 0.7178777393310266, 1.0),
    (0.6290657439446367, 0.8554248366013072, 0.7197231833910035, 1.0),
    (0.6235294117647059, 0.8533333333333334, 0.7215686274509804, 1.0),
    (0.6179930795847751, 0.8512418300653595, 0.7234140715109574, 1.0),
    (0.6124567474048442, 0.8491503267973857, 0.7252595155709343, 1.0),
    (0.6069204152249135, 0.8470588235294118, 0.7271049596309113, 1.0),
    (0.6013840830449828, 0.844967320261438, 0.7289504036908881, 1.0),
    (0.5958477508650519, 0.842875816993464, 0.730795847750865, 1.0),
    (0.590311418685121, 0.8407843137254902, 0.732641291810842, 1.0),
    (0.5847750865051903, 0.8386928104575164, 0.7344867358708189, 1.0),
    (0.5792387543252595, 0.8366013071895425, 0.7363321799307959, 1.0),
    (0.5737024221453287, 0.8345098039215687, 0.7381776239907728, 1.0),
    (0.568166089965398, 0.8324183006535948, 0.7400230680507498, 1.0),
    (0.5626297577854671, 0.830326797385621, 0.7418685121107267, 1.0),
    (0.5570934256055364, 0.8282352941176472, 0.7437139561707036, 1.0),
    (0.5515570934256055, 0.8261437908496733, 0.7455594002306806, 1.0),
    (0.5460207612456748, 0.8240522875816993, 0.7474048442906575, 1.0),
    (0.540484429065744, 0.8219607843137255, 0.7492502883506345, 1.0),
    (0.5349480968858131, 0.8198692810457516, 0.7510957324106113, 1.0),
    (0.5294117647058824, 0.8177777777777778, 0.7529411764705882, 1.0),
    (0.5238754325259516, 0.8156862745098039, 0.7547866205305652, 1.0),
    (0.5183391003460207, 0.8135947712418301, 0.7566320645905421, 1.0),
    (0.51280276816609, 0.8115032679738563, 0.758477508650519, 1.0),
    (0.5072664359861592, 0.8094117647058824, 0.760322952710496, 1.0),
    (0.5017301038062284, 0.8073202614379086, 0.7621683967704729, 1.0),
    (0.49619377162629763, 0.8052287581699347, 0.7640138408304499, 1.0),
    (0.4906574394463668, 0.8031372549019609, 0.7658592848904268, 1.0),
    (0.485121107266436, 0.801045751633987, 0.7677047289504038, 1.0),
    (0.4795847750865052, 0.7984621299500193, 0.7695501730103806, 1.0),
    (0.4740484429065744, 0.7953863898500577, 0.7713956170703576, 1.0),
    (0.4685121107266436, 0.7923106497500961, 0.7732410611303345, 1.0),
    (0.4629757785467128, 0.7892349096501345, 0.7750865051903114, 1.0),
    (0.4574394463667822, 0.7861591695501732, 0.7769319492502883, 1.0),
    (0.4519031141868512, 0.7830834294502115, 0.7787773933102653, 1.0),
    (0.4463667820069204, 0.7800076893502499, 0.7806228373702422, 1.0),
    (0.4408304498269896, 0.7769319492502884, 0.7824682814302192, 1.0),
    (0.43529411764705883, 0.7738562091503268, 0.7843137254901961, 1.0),
    (0.42975778546712806, 0.7707804690503652, 0.7861591695501731, 1.0),
    (0.42422145328719724, 0.7677047289504038, 0.78800461361015, 1.0),
    (0.41868512110726647, 0.7646289888504422, 0.7898500576701268, 1.0),
    (0.41314878892733564, 0.7615532487504806, 0.7916955017301038, 1.0),
    (0.40761245674740487, 0.758477508650519, 0.7935409457900807, 1.0),
    (0.40207612456747405, 0.7554017685505575, 0.7953863898500577, 1.0),
    (0.3965397923875433, 0.7523260284505959, 0.7972318339100346, 1.0),
    (0.39100346020761245, 0.7492502883506343, 0.7990772779700115, 1.0),
    (0.3854671280276817, 0.7461745482506728, 0.8009227220299885, 1.0),
    (0.37993079584775086, 0.7430988081507113, 0.8027681660899654, 1.0),
    (0.3743944636678201, 0.7400230680507497, 0.8046136101499424, 1.0),
    (0.36885813148788943, 0.7369473279507882, 0.8064590542099191, 1.0),
    (0.3633217993079585, 0.7338715878508266, 0.8083044982698961, 1.0),
    (0.3577854671280277, 0.730795847750865, 0.8101499423298731, 1.0),
    (0.3522491349480969, 0.7277201076509034, 0.81199538638985, 1.0),
    (0.3467128027681661, 0.724644367550942, 0.8138408304498269, 1.0),
    (0.3411764705882353, 0.7215686274509804, 0.8156862745098039, 1.0),
    (0.33564013840830453, 0.7184928873510188, 0.8175317185697808, 1.0),
    (0.3301038062283737, 0.7154171472510572, 0.8193771626297578, 1.0),
    (0.3245674740484429, 0.7123414071510957, 0.8212226066897347, 1.0),
    (0.3190311418685121, 0.7092656670511341, 0.8230680507497116, 1.0),
    (0.31349480968858134, 0.7061899269511726, 0.8249134948096886, 1.0),
    (0.3079584775086506, 0.703114186851211, 0.8267589388696654, 1.0),
    (0.3031910803537101, 0.6989619377162629, 0.825836216839677, 1.0),
    (0.29888504421376394, 0.6941637831603229, 0.8232525951557093, 1.0),
    (0.29457900807381776, 0.6893656286043829, 0.8206689734717416, 1.0),
    (0.2902729719338716, 0.6845674740484429, 0.8180853517877739, 1.0),
    (0.28596693579392557, 0.679769319492503, 0.8155017301038062, 1.0),
    (0.2816608996539793, 0.6749711649365628, 0.8129181084198385, 1.0),
    (0.2773548635140331, 0.6701730103806228, 0.8103344867358708, 1.0),
    (0.2730488273740869, 0.6653748558246828, 0.8077508650519031, 1.0),
    (0.26874279123414074, 0.6605767012687428, 0.8051672433679353, 1.0),
    (0.26443675509419456, 0.6557785467128028, 0.8025836216839677, 1.0),
    (0.2601307189542484, 0.6509803921568628, 0.7999999999999999, 1.0),
    (0.2558246828143022, 0.6461822376009227, 0.7974163783160323, 1.0),
    (0.25151864667435603, 0.6413840830449827, 0.7948327566320645, 1.0),
    (0.24721261053440985, 0.6365859284890427, 0.7922491349480969, 1.0),
    (0.24290657439446367, 0.6317877739331026, 0.7896655132641291, 1.0),
    (0.23860053825451752, 0.6269896193771627, 0.7870818915801615, 1.0),
    (0.2342945021145713, 0.6221914648212226, 0.7844982698961938, 1.0),
    (0.22998846597462516, 0.6173933102652825, 0.781914648212226, 1.0),
    (0.22568242983467898, 0.6125951557093425, 0.7793310265282584, 1.0),
    (0.2213763936947328, 0.6077970011534025, 0.7767474048442906, 1.0),
    (0.21707035755478676, 0.6029988465974626, 0.774163783160323, 1.0),
    (0.21276432141484047, 0.5982006920415225, 0.7715801614763552, 1.0),
    (0.2084582852748943, 0.5934025374855825, 0.7689965397923876, 1.0),
    (0.20415224913494812, 0.5886043829296425, 0.7664129181084198, 1.0),
    (0.19984621299500194, 0.5838062283737024, 0.7638292964244522, 1.0),
    (0.19554017685505576, 0.5790080738177624, 0.7612456747404844, 1.0),
    (0.19123414071510958, 0.5742099192618224, 0.7586620530565167, 1.0),
    (0.1869281045751634, 0.5694117647058824, 0.756078431372549, 1.0),
    (0.18262206843521722, 0.5646136101499424, 0.7534948096885813, 1.0),
    (0.17831603229527107, 0.5598154555940024, 0.7509111880046137, 1.0),
    (0.1740099961553249, 0.5550173010380623, 0.7483275663206459, 1.0),
    (0.1697039600153787, 0.5502191464821223, 0.7457439446366783, 1.0),
    (0.16539792387543253, 0.5456978085351788, 0.7434371395617071, 1.0),
    (0.16109188773548636, 0.5412687427912342, 0.7412226066897347, 1.0),
    (0.15678585159554018, 0.5368396770472895, 0.7390080738177625, 1.0),
    (0.15247981545559403, 0.5324106113033449, 0.7367935409457901, 1.0),
    (0.14817377931564796, 0.5279815455594004, 0.7345790080738178, 1.0),
    (0.14386774317570167, 0.5235524798154556, 0.7323644752018454, 1.0),
    (0.1395617070357555, 0.519123414071511, 0.7301499423298732, 1.0),
    (0.1352556708958093, 0.5146943483275663, 0.7279354094579008, 1.0),
    (0.13094963475586313, 0.5102652825836217, 0.7257208765859285, 1.0),
    (0.12664359861591695, 0.505836216839677, 0.7235063437139562, 1.0),
    (0.12233756247597079, 0.5014071510957324, 0.7212918108419839, 1.0),
    (0.11803152633602461, 0.4969780853517878, 0.7190772779700115, 1.0),
    (0.11372549019607844, 0.49254901960784314, 0.7168627450980393, 1.0),
    (0.10941945405613226, 0.4881199538638985, 0.7146482122260669, 1.0),
    (0.10511341791618609, 0.48369088811995387, 0.7124336793540946, 1.0),
    (0.10080738177623991, 0.4792618223760092, 0.7102191464821223, 1.0),
    (0.09650134563629374, 0.4748327566320646, 0.70800461361015, 1.0),
    (0.09219530949634756, 0.47040369088811995, 0.7057900807381776, 1.0),
    (0.08788927335640138, 0.4659746251441753, 0.7035755478662054, 1.0),
    (0.0835832372164552, 0.4615455594002307, 0.701361014994233, 1.0),
    (0.07927720107650915, 0.45711649365628615, 0.6991464821222607, 1.0),
    (0.07497116493656286, 0.4526874279123414, 0.6969319492502883, 1.0),
    (0.07066512879661668, 0.44825836216839676, 0.6947174163783161, 1.0),
    (0.06635909265667052, 0.4438292964244521, 0.6925028835063437, 1.0),
    (0.06205305651672434, 0.4394002306805075, 0.6902883506343714, 1.0),
    (0.05774702037677816, 0.43497116493656285, 0.6880738177623991, 1.0),
    (0.05344098423683198, 0.4305420991926182, 0.6858592848904268, 1.0),
    (0.04913494809688582, 0.4261130334486736, 0.6836447520184545, 1.0),
    (0.04482891195693964, 0.42168396770472893, 0.6814302191464822, 1.0),
    (0.04052287581699346, 0.4172549019607843, 0.6792156862745098, 1.0),
    (0.03621683967704728, 0.41282583621683966, 0.6770011534025375, 1.0),
    (0.0319108035371011, 0.408396770472895, 0.6747866205305653, 1.0),
    (0.03137254901960784, 0.4035371011149558, 0.6698808150711265, 1.0),
    (0.03137254901960784, 0.3986159169550173, 0.6645905420991927, 1.0),
    (0.03137254901960784, 0.39369473279507883, 0.6593002691272588, 1.0),
    (0.03137254901960784, 0.38877354863514035, 0.654009996155325, 1.0),
    (0.03137254901960784, 0.383852364475202, 0.6487197231833912, 1.0),
    (0.03137254901960784, 0.37893118031526335, 0.6434294502114571, 1.0),
    (0.03137254901960784, 0.3740099961553249, 0.6381391772395233, 1.0),
    (0.03137254901960784, 0.3690888119953864, 0.6328489042675894, 1.0),
    (0.03137254901960784, 0.36416762783544787, 0.6275586312956556, 1.0),
    (0.03137254901960784, 0.3592464436755094, 0.6222683583237216, 1.0),
    (0.03137254901960784, 0.3543252595155709, 0.6169780853517878, 1.0),
    (0.03137254901960784, 0.34940407535563245, 0.6116878123798539, 1.0),
    (0.03137254901960784, 0.344482891195694, 0.6063975394079201, 1.0),
    (0.03137254901960784, 0.3395617070357555, 0.6011072664359862, 1.0),
    (0.03137254901960784, 0.33464052287581697, 0.5958169934640523, 1.0),
    (0.03137254901960784, 0.3297193387158785, 0.5905267204921184, 1.0),
    (0.03137254901960784, 0.32479815455594, 0.5852364475201846, 1.0),
    (0.03137254901960784, 0.31987697039600155, 0.5799461745482507, 1.0),
    (0.03137254901960784, 0.314955786236063, 0.5746559015763169, 1.0),
    (0.03137254901960784, 0.31003460207612454, 0.5693656286043829, 1.0),
    (0.03137254901960784, 0.30511341791618624, 0.5640753556324491, 1.0),
    (0.03137254901960784, 0.3001922337562476, 0.5587850826605152, 1.0),
    (0.03137254901960784, 0.2952710495963091, 0.5534948096885813, 1.0),
    (0.03137254901960784, 0.29034986543637065, 0.5482045367166475, 1.0),
    (0.03137254901960784, 0.2854286812764321, 0.5429142637447135, 1.0),
    (0.03137254901960784, 0.28050749711649364, 0.5376239907727797, 1.0),
    (0.03137254901960784, 0.27558631295655517, 0.5323337178008458, 1.0),
    (0.03137254901960784, 0.2706651287966167, 0.527043444828912, 1.0),
    (0.03137254901960784, 0.26574394463667816, 0.5217531718569781, 1.0),
    (0.03137254901960784, 0.2608227604767397, 0.5164628988850442, 1.0),
    (0.03137254901960784, 0.2559015763168012, 0.5111726259131103, 1.0),
    (0.03137254901960784, 0.25098039215686274, 0.5058823529411764, 1.0),
]

default_event = {
    "names": {
        "0": "frequent",
        "1": "champion",
        "2": "nurturing_customer",
        "3": "low_value_frequent",
        "4": "hibernating",
        "5": "tending_to_lapse",
        "6": "new nurturing_customer",
        "7": "loyal_joe",
        "8": "new frequent",
        "9": "new champion",
        "10": "new potential_loyalist",
        "11": "new big_spender",
        "12": "big_spender",
    },
    "sizes": {
        "0": 109160,
        "1": 88294,
        "2": 58516,
        "3": 20583,
        "4": 18788,
        "5": 18240,
        "6": 14968,
        "7": 14170,
        "8": 8436,
        "9": 3977,
        "10": 2811,
        "11": 814,
        "12": 20,
    },
    "x": {
        "0": 0.5,
        "1": 0.6864285,
        "2": 0.5000085,
        "3": 0.0,
        "4": 5.3e-05,
        "5": 0.000658,
        "6": 0.5,
        "7": 0.0,
        "8": 0.5,
        "9": 0.765778,
        "10": 0.501067,
        "11": 1.0,
        "12": 1.0,
    },
    "y": {
        "0": 0.5323425,
        "1": 0.993567,
        "2": 0.4999915,
        "3": 0.5,
        "4": 0.0,
        "5": 0.2350875,
        "6": 0.5,
        "7": 0.2436135,
        "8": 0.9576815,
        "9": 0.997737,
        "10": 1.0,
        "11": 0.9987715,
        "12": 0.925,
    },
    "colors": {
        "0": 0.5,
        "1": 0.6864285,
        "2": 0.5000085,
        "3": 0.0,
        "4": 5.3e-05,
        "5": 0.000658,
        "6": 0.5,
        "7": 0.0,
        "8": 0.5,
        "9": 0.765778,
        "10": 0.501067,
        "11": 1.0,
        "12": 1.0,
    },
    "values": {
        "0": 0.876507,
        "1": 0.870852,
        "2": 0.6734655,
        "3": 0.8724435,
        "4": 1.0,
        "5": 0.8206965,
        "6": 0.0,
        "7": 0.9957305,
        "8": 0.0,
        "9": 0.0,
        "10": 0.0,
        "11": 0.0,
        "12": 0.625,
    },
}


def handler(event=None, context=None):
    if event is None:
        return json.dumps(None)
    if event.get("test"):
        event = default_event

    names = event.get("names")
    sizes = event.get("sizes")
    x_align = event.get("x")
    y_align = event.get("y")
    colors = event.get("colors")  # input should be normalized to [0, 1]
    values = event.get("values")

    keys = [k for k in names]
    keys.sort()

    names = [names[k] for k in keys]
    sizes = [sizes[k] for k in keys]
    x_align = [x_align[k] for k in keys]
    y_align = [y_align[k] for k in keys]
    colors = [colors[k] for k in keys]
    values = [values[k] for k in keys]

    colors = np.array(c)[list(map(int, colors * 255))]

    output = tp.aligned_treemap(
        sizes,
        x_align=x_align,
        y_align=y_align,
        x=0,
        y=0,
        dx=100,
        dy=100,
        labels=names,
        colors=colors,
    )
    return json.dumps(output)
