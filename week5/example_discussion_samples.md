# Week 5: 탑티어 저널 Discussion 예시 모음

> **목적**: Nature/Science급 Discussion의 실제 사례를 통해 3-Level Claim Hierarchy, Theoretical Contribution, Limitation Reframing 전략을 학습

---

## 샘플 1: 사회 인지 - Indebtedness (Nature Communications, 2024)

**논문 정보**:
- **제목**: The psychological, computational, and neural foundations of indebtedness
- **저널**: Nature Communications
- **링크**: https://www.nature.com/articles/s41467-023-44286-9

**이 Discussion의 우수한 점**:
| 요소 | 분석 |
|------|------|
| **3-Level Claim** | L1 (behavioral data) → L3 (mechanism: appraisal theory) 전환 명확 |
| **Theoretical contribution** | Appraisal Theory + Psychological Game Theory 통합 |
| **Computational modeling** | 감정을 수학적 모델로 형식화 |
| **Neural validation** | 행동 + 자기보고 + 뇌영상 삼중 검증 |
| **Limitation → Future** | 문화차이, 모델 한계를 구체적 후속연구로 전환 |

### Discussion 전문

Gift-giving, favor-exchanges, and providing assistance are behavioral expressions of relationships between individuals or groups. While favors from friends and family often engender reciprocity and gratitude, they can also elicit guilt in a beneficiary who may feel that they have burdened a benefactor. Favors in more transactive relationships, however, can evoke a sense of obligation in the beneficiary to repay the favor. In this study, we sought to develop a conceptual model of indebtedness that outlines how appraisals about the intentions behind a favor are critical to the generation of these distinct feelings, which in turn motivates how willing individuals are to accept or reject help and ultimately reciprocate the favor.

We provide a systematic validation of this conceptual model of indebtedness across three separate experiments by combining a large-scale online questionnaire, behavioral measurements in an interpersonal game, computational modeling, and neuroimaging. First, we used an open-ended survey to capture lay intuitions about indebtedness based on regression analysis of past emotional experiences and topic modeling based-text analysis of self-reported definitions. Overall, we find strong support that the feeling of indebtedness can be further separated into two distinct components—guilt for burdening the favor-doer and obligation to repay the favor. Using topic modeling on lay definitions of indebtedness, we find that guilt and gratitude appear to load on the same topic, while feeling words pertaining to burden and negative body states load on a separate topic. Second, we used a laboratory task designed to elicit indebtedness in the context of an interpersonal interaction and specifically manipulated information intended to shift the benefactor's perceptions of the beneficiary's intentions underlying their decisions. Although our manipulation was subtle, we find that it was able to successfully change participants' appraisals about how much the beneficiary cared about them and their beliefs about how much money the benefactor expected in return. Consistent with appraisal theory, these shifts in appraisals influenced participants' subjective feelings and ultimately their behaviors. Intentions perceived to be altruistic led to increased guilt and gratitude, while intentions viewed as more strategic increased feelings of obligation. While all three feelings increased reciprocity decisions, the guilt and obligation components of indebtedness increased the probability of rejecting help when that option was available to the participant.

One contribution of this work is the use of computational modeling to predict reciprocity and help-acceptance decisions in our interpersonal task based on our conceptual model of indebtedness. The majority of empirical research on indebtedness and other emotions has relied on participants' self-reported feelings in response to explicit questions regarding social emotions, which has significant limitations, such as its dependence on participants' ability to introspect. Formalizing emotions using computational models is critical to advancing theory, characterizing their impact on behavior, and identifying associated neural and physiological substrates. However, the application of computational modeling to the study of social emotions is a relatively new enterprise. Previous research has had success modeling belief-dependent utility using Psychological Game Theory in interactive social contexts. Building on this work, we model participants' appraisals and emotions based on the state of the game to predict two different types of decisions (i.e., reciprocity & help-acceptance). The current work contributes to a growing family of game theoretic models of social emotions such as guilt, gratitude, and anger, and can be used to infer feelings in the absence of self-report, providing avenues for investigating other social emotions.

We provide a rigorous validation of our computational models using behaviors in the interpersonal game, self-reported subjective experiences, and neuroimaging. First, we can accurately predict participants' reciprocity and help-acceptance decisions. Second, we observed that the model predictions of second-order belief and perceived care in the reciprocity model accurately captured participant's trial-to-trial self-reported appraisal and feeling ratings. Third, our brain imaging analyses demonstrate that each feeling reflects a distinct psychological process, and that intention inference plays a key role during this process. Consistent with previous work on guilt and gratitude, our model representation of communal concern correlated with increased activity in the insula, dlPFC, and default mode network including the vmPFC and precuneus. Obligation, in contrast, captured participants' second order beliefs about expectations of repayment and correlated with increased activation in regions routinely observed in mentalizing including the dmPFC and TPJ.

We provide an even stronger test of our ability to characterize the neural processes associated with indebtedness by deriving a "neural utility" model. Previous work has demonstrated that it is possible to build brain models of preferences that can predict behaviors and the hidden motives behind the behaviors. Here, we trained multivoxel patterns of brain activity to predict participants' communal and obligation utility. We then used these brain-derived representations of communal concern and obligation to predict how much money participants ultimately reciprocated to the beneficiary. Remarkably, we found that this neural utility model of indebtedness was able to predict individual decisions entirely from brain activity and numerically outperformed (but not significantly) a control model that provided a theoretical upper bound of how well reciprocity behavior can be predicted directly from brain activity. Importantly, the neural utility model was able to accurately capture each participant's preference for communal concern relative to obligation. We observed a significant drop in our ability to predict behavior when we randomly shuffled the weighting parameter across participants. In addition, we find that the more the pattern of brain activity predicting reciprocity behavior resembled brain patterns predictive of communal concern or obligation, the more our behavioral computational model weighted this feeling in predicting behavior, demonstrating that these distinct appraisals/feelings are involved in motivating reciprocity decisions.

This work advances our theoretical understanding of social emotions. First, we highlight the complex relationship between gratitude and indebtedness. We propose that feeling cared for by a benefactor, which we call communal concern, is comprised of both guilt and gratitude. Each emotion diverges in valence, with gratitude being positive, and guilt being negative, but both promote reciprocity behavior. When faced with the offer of help, anticipated gratitude should motivate the beneficiary to accept help in order to establish or promote a relationship, whereas anticipated guilt should motivate the beneficiary to reject help out of concern to protect the benefactor from incurring a cost. Although we observed support for this prediction, our interpersonal task was not designed to explicitly differentiate guilt from gratitude, which limited the ability of our reciprocity model to capture the specific contributions of guilt and gratitude to communal concern and likely impacted identifiability of the parameters of the help-acceptance model. Future work might continue to refine the relationship between these two aspects of communal concern both in terms of behaviors in experiments and computations in models.

Second, our conceptual model provides a framework to better understand the role of relationships and contexts in generating feelings of indebtedness within a single individual. Different types of relationships (see Clark and Mills's theory of communal and exchange relationships, and Alan Fiske's Relational Models Theory) have been theorized to emphasize different goals and social norms which can impact social emotions. For example, communal relationships prioritize the greater good of the community and are more conducive to altruistic sharing, which can be signaled by altruistic favors. In contrast, exchange relationships are more transactional in nature and emphasize maintaining equity in the relationship, which can be signaled by strategic favors. Our conceptual model proposes that perceptions of the benefactor's intentions directly impact the feelings experienced by the beneficiary (e.g., guilt & obligation). Although we deliberately attempted to minimize aspects of the relationship between the benefactor and beneficiary by making players anonymous to control for reputational effects, future work might experimentally manipulate these relationships to directly test the hypothesis that relationship types differentially moderate the responses of gratitude and subcomponents of indebtedness.

Third, we present evidence exploring the relationship between indebtedness and guilt. Guilt and indebtedness are interesting emotions in that they are both negatively valenced, yet promote prosocial behaviors. In previous work, we have operationalized guilt as arising from disappointing a relationship partner's expectations, which is conceptually related to the feeling of obligation in this paper. This feeling results from disappointing a relationship partner or violating a norm of reciprocity and is a motivational sentiment evoked by social expectations reflecting a "sense of should" that is associated with other negative affective responses such as feelings of pressure, burden, anxiety, and even resentment. In other work, we have investigated how guilt can arise from causing unintended harm to a relationship partner. This is conceptually more similar to how we frame guilt here, which arises from the feeling that one has unnecessarily burdened a relationship partner even though the help was never explicitly requested by the beneficiary. We believe that continuing efforts to refine mathematical models of emotions across a range of contexts, will eventually allow the field to move beyond relying on the restrictive and imprecise semantics of linguistic labels to define emotion categories (e.g., guilt, gratitude, indebtedness, obligation, feeling, motivation, etc.).

Our study has several potential limitations, which are important to acknowledge. First, although we directly and conceptually replicate our key findings across multiple samples, all of our experiments recruit experimental samples from a Chinese population. It is possible that there are cultural differences in the experience of indebtedness, which may not generalize to other parts of the world. For example, compared with Westerners who commonly express gratitude when receiving benevolent help, Japanese participants (East Asian population) often respond with "Thank you" or "I am sorry", indicating their higher experience of guilt after receiving favors. Cultural differences may perhaps reflect how the two components of indebtedness are weighted, with guilt being potentially more prominent in East Asian compared to Western populations, reflecting broader cultural differences in collectivism and individualism. Second, our computational models may oversimplify the appraisal and emotion generating processes. These models operationalize the appraisals of perceived care and second-order belief using information available to each participant in the task (i.e., benefactor's helping behavior and manipulation about the participant's ability to reciprocate), which may not generalize to other experimental contexts without modification. Although our computational models performed well in capturing participants' behaviors in this task, we emphasize the importance of continued refinement. Third, future research is needed to extend our conceptual model by differentiating different types of help-receiving events (e.g., help when moving to a new apartment vs. help during a period of sickness) and manipulating other related contexts, such as gift-receiving and help-seeking.

In summary, in this study, we develop a comprehensive and systematic conceptual model of indebtedness and validate it across three studies combining a large-scale online questionnaire, an interpersonal game, computational modeling and neuroimaging. A key aspect to this work is the emphasis on the role of appraisals about the intentions behind a favor in generating distinct feelings of guilt and obligation, which in turn motivates how willing beneficiaries are to accept or reject help and ultimately reciprocate the favor. Together, these findings highlight the psychological, computational, and neural mechanisms underlying the hidden costs of receiving favors.

---

## 샘플 2: 사회 학습 - Empathy 전파 (PNAS, 2024)

**논문 정보**:
- **제목**: The social transmission of empathy relies on observational reinforcement learning
- **저널**: PNAS
- **링크**: https://www.pnas.org/doi/abs/10.1073/pnas.2313073121

**이 Discussion의 우수한 점**:
| 요소 | 분석 |
|------|------|
| **Opening** | "provide mechanistic insights" - L3 수준에서 시작 |
| **Policy implication** | 학문적 발견 → 정책 함의로 확장 |
| **Alternative explanations** | 대안 설명 체계적 배제 (imitation, conformity 등) |
| **Neural mechanism** | TPJ-AI connectivity로 메커니즘 구체화 |
| **Limitation** | 샘플 제한 (young female) 솔직히 인정 |

### Discussion 전문

The assumption that empathy can be transmitted between individuals forms the basis of influential theories of moral development. Here, we provide mechanistic insights into the social transmission of empathy. Confirmed in three independent studies and substantiated by a control study, our results showed that empathy is transmitted by learning from observed empathic reactions of others. The observational learning of empathy can increase or decrease empathy in the observer, depending on the role model the participants learn from. Notably, the learning-related changes in empathy were elicited by observing empathic responses of an unknown, random individual, and expressed themselves on the subjective (empathy ratings) and neural level (connectivity between TPJ and an AI region that correlated with trial-by-trial empathy ratings as well as the neural activity of the AI region). This indicates that the social transmission of empathy occurs in "random" social interactions and changes the neural responses to the misfortune of others, here their pain.

The finding that observing empathic responses in others changes empathic responses in the observer is important, because empathy is commonly related to an increase in prosocial behavior. In line with these findings, the learning-related increase in empathy ratings was related to an increase in participants' willingness to invest time to help another person. From a policy point of view, these results suggest that creating a highly empathic environment may enhance prosocial tendencies. On the flipside, our findings also show that the presence of non-empathic individuals can undermine empathy and prosocial motivation.

It has been shown before that empathy ratings of a group can shift individual empathic feelings and influence donations to a homeless shelter. Moreover, a recent study in a clinical setting showed that the assessment of a person's pain by senior medical students is influenced by the opinion of other medical doctors, especially if they are unsure about the authenticity of the person's pain responses. Going beyond these previous results, our study reveals a mechanism through which empathy is transmitted across individuals. We show that the extent to which people change their subjective and neural responses to the pain of others is predicted by the weight they give to the prediction-error signal generated by the discrepancy between expected and observed empathy ratings of others. Specifically, our results show that participants generate positive observational prediction errors if human demonstrators display a stronger empathic reaction than expected, and, as a result, increase their empathy ratings. In contrast, being confronted with individuals who show less empathy than expected results in negative prediction errors and a decrease in empathy ratings of the observer.

In addition, participants in the high and low empathy groups predominantly updated their values based on positive and negative observational prediction errors, respectively. Substantiating these findings, additional analyses showed stronger learning for positive compared to negative prediction errors in the high empathy group and the reverse pattern for the low empathy group. Previous research showed that people may perform precision weighting to discount atypical prediction errors. In the context of these results, the asymmetric updating here may reflect the discounting of atypical prediction errors (e.g., negative prediction errors in the high and positive prediction errors in the low empathy group) to maintain the initial changes in empathy ratings.

It is well established that observational learning parameters can predict differences in socially relevant phenomena such as the social transmission of fear, and the social modulation of risk and choice preferences. In influential theoretical models, observational learning has long been assumed to constitute a mechanism for the social transmission of empathy. Providing empirical evidence for this notion, we show that an observational learning model can predict the extent to which empathy is transmitted from one individual (i.e., the demonstrator) to another (i.e., the observer) and applied by the observer to third parties uninvolved in the learning process (generalization).

We find that learning from observing other's empathic reactions does not only change participants' empathy ratings, but also their neural responses to other's pain. Specifically, the weight participants assigned to observational prediction errors modulated connectivity between regions associated with observational learning, such as the TPJ, and regions associated with the processing of other's pain, such as the AI. Taking an individual difference perspective, the more strongly a person weighted the observational prediction errors, the stronger the coupling of left TPJ–AI in the high empathy group, and the weaker the TPJ–AI coupling in the low empathy group. Apart from this, the individual differences in the magnitude of observational learning (i.e., weight parameter) also modulated the neural activations in the AI. Thus, the empathy shown by the role model modulated the way in which observational prediction error weights affected brain connectivity.

The finding of the processing of observational prediction errors in the left TPJ is in line with recent evidence linking this region to social influence on reward learning and prosocial decision making. Extending these previous results, our findings show that learning by observing high and low empathic individuals modulates the connectivity between the left TPJ and the AI as well as the vmPFC. Importantly, the AI region that was modulated by learning also significantly correlated with the trial-by-trial empathy ratings in the baseline session. Therefore, observational learning indeed changed the processing of other's pain in the AI, i.e., a region that forms a central part of the empathy network.

Neural responses in the vmPFC have been related to value computation in general, and in particular, to the computation of the value of pain. Given the present findings, it is possible that observing empathic responses of others changes participants' valuation of the pain of others to justify an increase or decrease in participants own empathy ratings. Together, our neural findings uncover a neural mechanism for the social transmission of empathy that can explain the plasticity of empathic responses in different social environments.

Although we show a change in empathy ratings and neural responses to the pain of others that is closely predicted by learning parameters, alternative explanations to observational learning have to be considered. First, the observed changes in subjective and neural empathy responses may reflect mere imitation of motor responses. The results of the non-social control study argue against this alternative explanation. Although participants paid attention to, and learned to predict, the computer-generated ratings equally well as those of the human demonstrators, they did not use the learned information to update their own empathy as much as with human demonstrators. Second, participants may have changed their ratings because they were instructed to predict the ratings of the demonstrator (resulting in an "implicit instruction" effect). Our results replicate learning-related changes in empathy when participants were not instructed to predict the demonstrators' ratings (Study 4), rendering the possibility unlikely that the observed effects mainly reflect implicit instruction demands. Third, it is possible that participants changed their empathy ratings to conform with the ratings of the demonstrator or may have shown higher empathy ratings in the high-empathy group to please the demonstrator or the experimenter. Testing these assumptions, we found no significant relationship between participants' ratings on a well-established conformity and social desirability scales and their changes of empathy ratings in the observational-learning-of-empathy task. In addition, in the behavioral replication studies, participants were seated alone during the experiment, such that they were unobserved and could not interact with the experimenter. Although this setting minimized the influence of social desirability, the findings still replicated the learning-related changes in empathy ratings observed in the fMRI study. Based on this evidence, and given that the estimates from our observational learning model fitted the changes in empathy ratings and neural responses to other's pain, observational learning is likely to contribute to the social transmission of empathy.

We report findings from four independent samples that all consisted of young female participants. This allowed us to control for unspecific gender effects (e.g., induced by gender-mixed pairings of participants and confederates), and well-established age differences in decision-making, prosocial tendencies, and the processing of rewards.

---

## 샘플 3: 인지 심리학 (추가 예정)

**후보 논문**:

| 논문 | 저널 | 연도 | 링크 |
|------|------|------|------|
| Using cognitive psychology to understand GPT-3 | PNAS | 2023 | [Link](https://www.pnas.org/doi/10.1073/pnas.2218523120) |
| Neural dynamics of shifting attention | PNAS | 2024 | [Link](https://www.pnas.org/doi/10.1073/pnas.2406061121) |
| Predicting human decisions with ML | Nature Human Behaviour | 2025 | [Link](https://www.nature.com/articles/s41562-025-02267-6) |

> **Note**: Discussion 텍스트 확보 후 추가 예정

---

## 학습 포인트 요약

### 1. 3-Level Claim Hierarchy 적용

**샘플 1 (Indebtedness)**:
- L1: "we find strong support that the feeling of indebtedness can be further separated..."
- L3: "these findings highlight the psychological, computational, and neural mechanisms..."

**샘플 2 (Empathy)**:
- L1: "our results showed that empathy is transmitted by learning..."
- L3: "provide mechanistic insights into the social transmission of empathy"

### 2. Theoretical Contribution 패턴

| 패턴 | 샘플 1 | 샘플 2 |
|------|--------|--------|
| Theory integration | Appraisal + Game Theory | Observational learning + Empathy |
| Mechanism proposal | Guilt vs Obligation 분리 | TPJ-AI connectivity |
| Model formalization | Computational model of emotions | Prediction error model |

### 3. Limitation → Future Direction 전환

**샘플 1**: "It is possible that there are cultural differences... Cultural differences may perhaps reflect how the two components of indebtedness are weighted"

**샘플 2**: "We report findings from four independent samples that all consisted of young female participants. This allowed us to control for..."

### 4. Cross-disciplinary Impact

- **샘플 1**: 심리학 + 경제학 (Game Theory) + 신경과학
- **샘플 2**: 도덕 발달 이론 + 학습 이론 + 정책 함의

---

## 수업 활용 가이드

### 활동 1: Claim Level 분석 (10분)
각 샘플에서 L1, L2, L3 문장을 찾아 표시하기

### 활동 2: Limitation Reframing 비교 (10분)
두 샘플의 Limitation 처리 방식 비교하고 자신의 연구에 적용

### 활동 3: Opening 문장 분석 (5분)
각 샘플의 첫 문단이 어떻게 연구의 significance를 establish하는지 분석
