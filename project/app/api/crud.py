from typing import Union

from app.models.pydantic import SummaryPayloadSchema
from app.models.tortoise_model import TextSummary


async def post(payload: SummaryPayloadSchema) -> int:
    summary = TextSummary(url=payload.url, summary="dummy summary")
    await summary.save()
    return summary.id


async def get(id: int) -> Union[dict, None]:
    summary = await TextSummary.filter(id=id).first().values()
    if summary:
        return summary
    return None


async def get_all() -> list:
    summaries = await TextSummary.all().values()
    return summaries


async def delete(id: int) -> int:
    summary = await TextSummary.filter(id=id).first().delete()
    return summary
