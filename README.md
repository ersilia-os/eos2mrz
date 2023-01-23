# DeepSMILES, an alternate SMILES representation for deep learning

DeepSMILES converts a SMILES string to a more accurate syntax for molecule representation, taking into account both the branches (closed parenthesis in the SMILES strings) and rings (using a single symbol at ring closure that also indicates ring size). This syntax is particularly suitable in generative models, when the output is a SMILES string. With DeepSMILES, scientists can train a network using this new syntax, generate new molecules represented as DeepSMILES and then decode them back to normal SMILES strings.

## Identifiers

* EOS model ID: `eos2mrz`
* Slug: `deepsmiles`

## Characteristics

* Input: `Compound`
* Input Shape: `Single`
* Task: `Generative`
* Output: `Compound`
* Output Type: `String`
* Output Shape: `Single`
* Interpretation: String representing a DeepSMILES

## References

* [Publication](https://chemrxiv.org/engage/api-gateway/chemrxiv/assets/orp/resource/item/60c73ed6567dfe7e5fec388d/original/deep-smiles-an-adaptation-of-smiles-for-use-in-machine-learning-of-chemical-structures.pdf)
* [Source Code](https://github.com/baoilleach/deepsmiles)
* Ersilia contributor: [brosular](https://github.com/brosular)

## Citation

If you use this model, please cite the [original authors](https://chemrxiv.org/engage/api-gateway/chemrxiv/assets/orp/resource/item/60c73ed6567dfe7e5fec388d/original/deep-smiles-an-adaptation-of-smiles-for-use-in-machine-learning-of-chemical-structures.pdf) of the model and the [Ersilia Model Hub](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff).

## License

This package is licensed under a GPL-3.0 license. The model contained within this package is licensed under a MIT license.

Notice: Ersilia grants access to these models 'as is' provided by the original authors, please refer to the original code repository and/or publication if you use the model in your research.

## About Us

The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission!