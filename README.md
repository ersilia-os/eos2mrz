# DeepSMILES, an alternate SMILES representation for deep learning

DeepSMILES converts a SMILES string to a more accurate syntax for molecule representation, taking into account both the branches (closed parenthesis in the SMILES strings) and rings (using a single symbol at ring closure that also indicates ring size). This syntax is particularly suitable in generative models, when the output is a SMILES string. With DeepSMILES, scientists can train a network using this new syntax, generate new molecules represented as DeepSMILES and then decode them back to normal SMILES strings.

This model was incorporated on 2022-07-28.

## Information
### Identifiers
- **Ersilia Identifier:** `eos2mrz`
- **Slug:** `deepsmiles`

### Domain
- **Task:** `Representation`
- **Subtask:** `Featurization`
- **Biomedical Area:** `Any`
- **Target Organism:** `Not Applicable`
- **Tags:** `Chemical language model`, `Chemical notation`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `1`
- **Output Consistency:** `Fixed`
- **Interpretation:** String representing a DeepSMILES

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| deepsmiles | string |  | DeepSMILES representation of the input molecule |


### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos2mrz](https://hub.docker.com/r/ersiliaos/eos2mrz)
- **Docker Architecture:** `AMD64`, `ARM64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos2mrz.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos2mrz.zip)

### Resource Consumption


### References
- **Source Code**: [https://github.com/baoilleach/deepsmiles](https://github.com/baoilleach/deepsmiles)
- **Publication**: [https://chemrxiv.org/engage/chemrxiv/article-details/60c73ed6567dfe7e5fec388d](https://chemrxiv.org/engage/chemrxiv/article-details/60c73ed6567dfe7e5fec388d)
- **Publication Type:** `Preprint`
- **Publication Year:** `2018`
- **Ersilia Contributor:** [brosular](https://github.com/brosular)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [MIT](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos2mrz
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos2mrz
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
