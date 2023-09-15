from pydantic import BaseModel, Field, model_validator, field_validator


class SomeType(BaseModel):
    some_field: str
    some_other_field: str = Field(..., alias="someOtherField")

    @field_validator("some_other_field")
    def validate_some_other_field(self, value: str) -> str:
        return value.upper()

    @model_validator(mode="after")
    def validate_some_field(self) -> "SomeType":
        self.some_field = self.some_field.upper()
        return self


def main():
    pass


if __name__ == "__main__":
    main()
